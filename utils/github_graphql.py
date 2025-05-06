import os
import base64
import random
import requests
from flask import Response
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

TOKEN = os.getenv("GH_TOKEN")
USERNAME = os.getenv("GH_USERNAME")

GQL_URL = "https://api.github.com/graphql"
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


def run_query(query: str, variables: dict = {}) -> dict:
    """Execute a GraphQL query and return the data."""
    response = requests.post(GQL_URL, json={"query": query, "variables": variables}, headers=HEADERS)
    if response.status_code != 200:
        raise Exception(f"GraphQL query failed: {response.text}")
    return response.json()["data"]


def get_general_stats(username: str) -> dict:
    """Fetch general GitHub stats for a given username."""
    query = """
    query($username: String!) {
      user(login: $username) {
        repositories(ownerAffiliations: OWNER, isFork: false, first: 100) {
          nodes { stargazerCount }
        }
        contributionsCollection {
          totalCommitContributions
          totalIssueContributions
          totalPullRequestContributions
          commitContributionsByRepository(maxRepositories: 100) {
            repository { name owner { login } }
          }
        }
      }
    }
    """
    data = run_query(query, {"username": username})
    user = data["user"]

    total_stars = sum(repo["stargazerCount"] for repo in user["repositories"]["nodes"])
    stats = user["contributionsCollection"]

    contributed_repos = [
        repo["repository"]
        for repo in stats["commitContributionsByRepository"]
        if repo["repository"]["owner"]["login"] != username
    ]

    return {
        "stars": total_stars,
        "commits": stats["totalCommitContributions"],
        "issues": stats["totalIssueContributions"],
        "prs": stats["totalPullRequestContributions"],
        "contributed": len(contributed_repos),
    }


def get_streak_and_contributions(username: str) -> dict:
    """Calculate total contributions, current streak, and top streak details."""
    query = """
    query($username: String!) {
      user(login: $username) {
        contributionsCollection {
          contributionCalendar {
            totalContributions
            weeks {
              contributionDays { contributionCount date }
            }
          }
        }
      }
    }
    """
    data = run_query(query, {"username": username})
    calendar = data["user"]["contributionsCollection"]["contributionCalendar"]

    total = calendar["totalContributions"]
    days = [d for week in calendar["weeks"] for d in week["contributionDays"]]
    today = datetime.now().date()

    # First contribution date
    first_contribution_date = next(
        (datetime.strptime(day["date"], "%Y-%m-%d").date() for day in days if day["contributionCount"] > 0),
        today
    )

    # Initialize variables
    current_streak = top_streak = temp_streak = 0
    top_start = top_end = temp_start = temp_end = None
    today_contribution = next((d["contributionCount"] for d in days if d["date"] == today.strftime("%Y-%m-%d")), 0)

    # Calculate top streak
    for day in reversed(days):
        date = datetime.strptime(day["date"], "%Y-%m-%d").date()
        count = day["contributionCount"]

        if count > 0:
            temp_start = temp_start or date
            temp_end = date
            temp_streak += 1
        else:
            if temp_streak > top_streak:
                top_streak = temp_streak
                top_start, top_end = temp_start, temp_end
            temp_streak = 0
            temp_start = temp_end = None

    if temp_streak > top_streak:
        top_streak = temp_streak
        top_start, top_end = temp_start, temp_end

    if top_start and top_end and top_start > top_end:
        top_start, top_end = top_end, top_start

    # Calculate current streak
    streak_start = streak_end = None
    counting = False

    for day in reversed(days):
        date = datetime.strptime(day["date"], "%Y-%m-%d").date()
        if date > today:
            continue

        if not counting:
            if (today_contribution > 0 and date == today) or (day["contributionCount"] > 0 and date == today - timedelta(days=1)):
                counting = True
                streak_start = streak_end = date
                current_streak += 1
        else:
            if day["contributionCount"] > 0:
                streak_start = date
                current_streak += 1
            else:
                break

    def format_date(date_obj: datetime.date, with_year: bool = False) -> str:
        return date_obj.strftime("%b %d, %Y") if with_year else date_obj.strftime("%b %d")

    return {
        "total_contributions": total,
        "first_contribution": format_date(first_contribution_date, with_year=True),
        "current_streak": current_streak,
        "current_streak_start": format_date(streak_start) if streak_start else "",
        "current_streak_end": format_date(streak_end) if streak_end else "",
        "top_streak": top_streak,
        "top_streak_start": format_date(top_start, with_year=True) if top_start else "",
        "top_streak_end": format_date(top_end, with_year=True) if top_end else "",
    }


def generate_ascii_bar(percentage: float, length: int = 7) -> str:
    """Generate an ASCII-style bar for the language chart."""
    filled = round((percentage / 100) * length)
    empty = length - filled
    return "■" * filled + "▢" * empty

def get_top_languages(username: str) -> dict:
    """Get top 5 programming languages used, with usage bars and percentages."""
    query = """
    query($username: String!) {
      user(login: $username) {
        repositories(ownerAffiliations: OWNER, isFork: false, first: 100) {
          nodes {
            languages(first: 10) {
              edges {
                size
                node { name color }
              }
            }
          }
        }
      }
    }
    """
    data = run_query(query, {"username": username})
    lang_usage = {}

    for repo in data["user"]["repositories"]["nodes"]:
        for edge in repo["languages"]["edges"]:
            lang = edge["node"]["name"]
            size = edge["size"]
            color = edge["node"].get("color") or "#ccc"

            if lang not in lang_usage:
                lang_usage[lang] = {"size": 0, "color": color}
            lang_usage[lang]["size"] += size

    sorted_langs = sorted(lang_usage.items(), key=lambda x: x[1]["size"], reverse=True)
    total_size = sum(info["size"] for info in lang_usage.values())

    top_languages = []
    for lang, info in sorted_langs[:5]:
        percentage = (info["size"] / total_size) * 100 if total_size else 0
        bar = generate_ascii_bar(percentage)
        percentage_str = f"{(percentage / 10):.2f}" if percentage < 1 else f"{percentage:.1f}"

        top_languages.append({
            "name": lang,
            "color": info["color"],
            "percentage": percentage_str,
            "bar": bar
        })

    return {"languages": top_languages}

WAKATIME_API_KEY = os.getenv("WAKA_API_KEY")

def get_waka_stats() -> dict:
    """Fetch WakaTime weekly stats and prepare data for SVG rendering."""
    if not WAKATIME_API_KEY:
        raise Exception("WAKA_API_KEY missing from environment variables.")

    today = datetime.now().date()
    weekday = today.weekday()  # Monday is 0, Sunday is 6

    # Find last Sunday
    days_since_sunday = (weekday + 1) % 7
    last_sunday = today - timedelta(days=days_since_sunday)

    url = (
        f"https://wakatime.com/api/v1/users/current/summaries"
        f"?start={last_sunday}&end={today}"
    )

    encoded_api_key = base64.b64encode((WAKATIME_API_KEY + ":").encode()).decode()
    headers = {
        "Authorization": f"Basic {encoded_api_key}",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"WakaTime API failed: {response.text}")

    raw_data = response.json()
    data = raw_data.get("data", [])

    if not data:
        raise Exception("No WakaTime data found.")

    # Today's coding time
    today_summary = next((day for day in data if day["range"]["date"] == str(today)), None)
    today_coding_time = today_summary["grand_total"]["text"] if today_summary else "0 mins"

    # Total coding time (Sunday -> Today)
    total_seconds = sum(day["grand_total"]["total_seconds"] for day in data)
    total_hours = total_seconds // 3600
    total_minutes = (total_seconds % 3600) // 60
    total_coding_time = f"{int(total_hours)} hrs {int(total_minutes)} mins"

    # Top language and top editor
    language_counter = {}
    editor_counter = {}

    for day in data:
        for language in day.get("languages", []):
            language_counter[language["name"]] = language_counter.get(language["name"], 0) + language["total_seconds"]
        for editor in day.get("editors", []):
            editor_counter[editor["name"]] = editor_counter.get(editor["name"], 0) + editor["total_seconds"]

    top_language = max(language_counter.items(), key=lambda x: x[1])[0] if language_counter else "N/A"
    top_editor = max(editor_counter.items(), key=lambda x: x[1])[0] if editor_counter else "N/A"

    # 7-day activity bar (Sunday → Saturday)
    activity_bar = []
    for day in data:
        seconds = day["grand_total"]["total_seconds"]
        if seconds >= 3600:
            activity_bar.append("■")
        else:
            activity_bar.append("▢")

    # Pad missing days AFTER the fetched days
    while len(activity_bar) < 7:
        activity_bar.append("▢")

    return {
        "today_coding_time": today_coding_time,
        "top_language": top_language,
        "top_editor": top_editor,
        "total_coding_time": total_coding_time,
        "activity_bar": "".join(activity_bar),
    }

def get_distro_info_stats(args):
    return {
        "username": args.get("username", "Yeswanth"),
        "distro": args.get("distro", "EndeavourOS x Git"),
        "shell": args.get("shell", "zsh + gh CLI"),
        "directory": args.get("directory", "projects"),
    }

def load_base64_gif(path):
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    return f"data:image/gif;base64,{encoded}"

def get_dev_pulse(args, username: str): 
    streak_data = get_streak_and_contributions(username)

    quotes = [
        "Push yourself, not just code.",
        "Break bugs, not hearts.",
        "One commit at a time.",
        "Ship it. Fix it later.",
        "Refactor life, not just code.",
        "Optimize for happiness.",
        "Merge peace, not conflicts.",
        "Deploy dreams, not doubts.",
        "Debug your mindset.",
        "Your only bug is doubt."
    ]

    current_mood = args.get('currentMood', '🎧 Focus Mode')
    current_focus = args.get('currentFocus', 'Terminal Converter')
    favorite_language = args.get('favoriteLanguage', 'Python')

    dev_pulse = {
        "current_mood": current_mood,
        "current_focus": current_focus,
        "favorite_language": favorite_language,
        "coding_streak": f"{streak_data['current_streak']} days 🔥",
        "terminal_quote": random.choice(quotes)
    }

    return dev_pulse

def svg_404():
    with open("static/img/404.png", "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode('utf-8')
    
    svg_content = f'''
    <svg xmlns="http://www.w3.org/2000/svg" width="400" height="200" viewBox="0 0 400 200">
        <style>
            text {{ 
                fill: white; 
                font-family: 'Ubuntu', sans-serif; 
                font-size: 20px; 
                text-anchor: middle;
                padding: 10px;
            }}
        </style>

        <!-- Embed the base64-encoded image -->
        <image href="data:image/png;base64,{img_base64}" x="15" y="10" width="370" height="170" />

        <!-- 404 Message -->
        <text x="200" y="200" class="message">
            404 - Not Found
        </text>
        
    </svg>
    '''
    return Response(svg_content, mimetype="image/svg+xml"), 404