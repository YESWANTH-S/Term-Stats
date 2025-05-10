import base64
import os
from flask import Flask, render_template, make_response, request
from utils.github_graphql import get_general_stats, get_streak_and_contributions, get_top_languages, get_waka_stats, get_distro_info_stats, get_dev_pulse, svg_404

# Constants
ALLOWED_STYLES = {"normal", "border", "raw"}
ALLOWED_GIF_MODES = {"true", "false", "static"}
USERNAME = os.getenv("GH_USERNAME")

app = Flask(__name__)

# Helper Functions
def load_base64_gif(path):
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    return f"data:image/gif;base64,{encoded}"

def load_base64_png(path):
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    return f"data:image/png;base64,{encoded}"

def get_color_params(request):
    return {
        "border_color": request.args.get("borderColor", "cdd6f4"),
        "title_color": request.args.get("titleColor", "cdd6f4"),
        "text_color": request.args.get("textColor", "cdd6f4"),
        "value_color": request.args.get("valueColor", "b4befe"),
        "current_streak_color": request.args.get("currentStreakColor", "b5a0f4"),
        "quote_color": request.args.get("quoteColor", "94e2d5"),
        "background_color": request.args.get("backgroundColor"),
    }

def make_svg_response(svg_content):
    response = make_response(svg_content)
    response.headers["Content-Type"] = "image/svg+xml"
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response

def generate_svg(template_name, context):
    svg = render_template(template_name, **context)
    return make_svg_response(svg)

def prepare_stats(base_gif_name, gif_key, default_username_required=True):
    style = request.args.get('style', 'normal')
    gif_mode = request.args.get('gif', 'true').lower()
    username = request.args.get('username', USERNAME if default_username_required else None)

    if style not in ALLOWED_STYLES:
        return svg_404()

    if gif_mode not in ALLOWED_GIF_MODES:
        return svg_404()

    stats = {}
    if gif_mode == "true":
        stats[gif_key] = load_base64_gif(f"static/img/{base_gif_name}.gif")
    elif gif_mode == "static":
        stats[gif_key] = load_base64_gif(f"static/img/{base_gif_name}.png")
    else:
        stats[gif_key] = ""

    stats["style"] = style
    stats["gif_mode"] = gif_mode

    return stats, username

# Routes
@app.route("/")
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        return f"Error in /: {e}", 500

@app.route("/basic")
def basic_svg():
    try:
        stats, username = prepare_stats("stats", "stats_base64_gif")
        stats.update(get_general_stats(username))
        stats.update(get_color_params(request))
        return generate_svg("general_stats.svg", stats)
    except Exception as e:
        return svg_404()

@app.route("/streaks")
def streak_svg():
    try:
        stats, username = prepare_stats("streaks", "streak_base64_gif")
        stats.update(get_streak_and_contributions(username))
        stats.update(get_color_params(request))
        return generate_svg("streak_stats.svg", stats)
    except Exception as e:
        return svg_404()

@app.route("/languages")
def languages_svg():
    try:
        stats, username = prepare_stats("lang", "lang_base64_gif")
        stats.update(get_top_languages(username))
        stats.update(get_color_params(request))
        return generate_svg("languages_stats.svg", stats)
    except Exception as e:
        return svg_404()

@app.route("/waka_stats")
def waka_stats_svg():
    try:
        stats, _ = prepare_stats("waka", "waka_base64_gif", default_username_required=False)
        stats.update(get_waka_stats())
        stats.update(get_color_params(request))
        return generate_svg("waka_stats.svg", stats)
    except Exception as e:
        return svg_404()

@app.route("/distro")
def distro_info_svg():
    try:
        stats, _ = prepare_stats("distro", "distro_base64_gif", default_username_required=False)
        stats.update(get_distro_info_stats(request.args))
        stats.update(get_color_params(request))
        return generate_svg("distro_info.svg", stats)
    except Exception as e:
        return svg_404()

@app.route("/dev_pulse")
def dev_pulse_svg():
    try:
        stats, username = prepare_stats("pulse", "pulse_base64_gif")
        stats.update(get_dev_pulse(request.args, username))
        stats.update(get_color_params(request))
        return generate_svg("dev_pulse.svg", stats)
    except Exception as e:
        return svg_404()

@app.route("/ping")
def ping():
    return "pong", 200

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
