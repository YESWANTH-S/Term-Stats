<p align="center">
  <h1 align="center">
    <img src="assets/Logo.ico" alt="Term-Stats Logo" width="100"/><br><b>Term-Stats</b>
  </h1>
</p>

<p align="center">
  <img src="assets/Term-Stat.gif" alt="Term-Stats Preview" width="65%"/>
</p>

<p align="center">
  Term-Stats provides customizable GitHub stats and metrics that you can embed in your README with a stylish terminal-inspired dashboard.<br>
  Track your GitHub activity, contributions, and development metrics easily!
</p>

<p align="center">
  <a href="https://term-stats.onrender.com/" target="_blank">
    <img src="https://img.shields.io/badge/Visit%20Website-Term%20Stats-b4befe?style=for-the-badge">
  </a>
</p>


## ✨ Features

<table>
  <thead>
    <tr>
      <th><strong>Feature</strong></th>
      <th><strong>Description</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>General Stats</strong></td>
      <td>Displays key metrics such as Stars, Commits, Pull Requests, Issues, and Repositories Contributed To.</td>
    </tr>
    <tr>
      <td><strong>Contribution Streaks</strong></td>
      <td>Tracks and displays your current streak, top streak, and total GitHub contributions.</td>
    </tr>
    <tr>
      <td><strong>Top Languages</strong></td>
      <td>Visualizes your most used programming languages with terminal-style progress bars.</td>
    </tr>
    <tr>
      <td><strong>WakaTime Coding Pulse</strong></td>
      <td>Shows coding data such as today’s coding time, top language, top editor, total weekly coding time, and a 7-day activity bar.</td>
    </tr>
    <tr>
      <td><strong>Developer Pulse</strong></td>
      <td>Displays customizable information about your mood, focus project, favorite programming language, distro, and current coding streak.</td>
    </tr>
    <tr>
      <td><strong>Distro Info Stats</strong></td>
      <td>Shows detailed information about your username, distribution, shell, root, and current directory, with options for customization via the UI.</td>
    </tr>
    <tr>
      <td><strong>GIF Integration</strong></td>
      <td>Offers three options for GIFs: animated GIFs, static images, or complete removal of GIFs.</td>
    </tr>
    <tr>
      <td><strong>UI-Based Customization</strong></td>
      <td>A new UI for easy customization, including:
        <ul>
          <li>Text color</li>
          <li>Value color</li>
          <li>Border color</li>
          <li>Current streak color</li>
          <li>Quotes color</li>
          <li>Background color</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><strong>One-Click Stat URL Generation</strong></td>
      <td>Simply enter your GitHub username, apply settings, and easily copy the generated SVG URLs for embedding.</td>
    </tr>
    <tr>
      <td><strong>Multiple Display Styles</strong></td>
      <td>Choose between different presentation styles for your stats:
        <ul>
          <li><code>border</code> — Rounded animated border around the stats.</li>
          <li><code>table</code> — Table-style format with animated dividers.</li>
          <li><code>raw</code> — Minimalist design without borders.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>


## 📸 Previews

### Single Stat Examples

<table>
  <tr>
    <td><b>Basic Stats</b></td>
    <td><b>Streak Stats</b></td>
    <td><b>Top Languages</b></td>
  </tr>
  <tr>
    <td><img src="https://term-stats.onrender.com/basic?style=raw" alt="Basic Stats" width="400"/></td>
    <td><img src="https://term-stats.onrender.com/streaks?style=raw" alt="Streak Stats" width="400"/></td>
    <td><img src="https://term-stats.onrender.com/languages?style=raw" alt="Top Languages" width="400"/></td>
  </tr>
</table>

<br>

<table>
  <tr>
    <td><b>WakaTime Stats</b></td>
    <td><b>Dev Pulse</b></td>
    <td><b>Distro Info</b></td>
  </tr>
  <tr>
    <td><img src="https://term-stats.onrender.com/waka_stats?style=raw" alt="WakaTime Stats" width="400"/></td>
    <td><img src="https://term-stats.onrender.com/dev_pulse?style=raw" alt="Dev Pulse" width="400"/></td>
    <td><img src="https://term-stats.onrender.com/distro?style=raw" alt="Top Languages" width="400"/></td>
  </tr>
</table>


### Different Styles (Border, Table, Transparent)

<table>
  <tr>
    <td><b>Border Style</b></td>
    <td><b>Table Style</b></td>
    <td><b>Transparent Style</b></td>
  </tr>
  <tr>
    <td><img src="https://term-stats.onrender.com/basic?style=border" alt="Border Style" width="400"/></td>
    <td><img src="https://term-stats.onrender.com/basic" alt="Table Style" width="400"/></td>
    <td><img src="https://term-stats.onrender.com/basic?style=raw" alt="Transparent Style" width="400"/></td>
  </tr>
</table>


### GIF Animation Example (With GIF, Static, Without GIF)

<table>
  <tr>
    <td><b>With GIF</b></td>
    <td><b>Static</b></td>
    <td><b>Without GIF</b></td>
  </tr>
  <tr>
    <td><img src="https://term-stats.onrender.com/streaks?style=raw" alt="Streaks with GIF" width="400"/></td>
    <td><img src="https://term-stats.onrender.com/streaks?style=raw&gif=static" alt="Streaks with GIF" width="400"/></td>
    <td><img src="https://term-stats.onrender.com/streaks?style=raw&gif=false" alt="Streaks without GIF" width="400"/></td>
  </tr>
</table>


## 🧪 Live Preview & Customization

Term-Stats now includes a built-in **UI Playground** that lets you preview and personalize your stats in real time.

  <img src="assets/Live.gif" alt="Term-Stats Preview" width="75%"/>

### 🎨 What You Can Customize:
- **Text Color**
- **Value Color**
- **Border & Background Colors**
- **Current Streak Color**
- **Quotes Color**
- **GIF Style** — choose between animated, static, or no GIFs
- **Input Fields** for:
  - **Developer Pulse:** Mood, Focus Project, Favorite Language, Distro
  - **Distro Info:** Username, Shell, Root, Directory

Enter your GitHub username, play around with settings, and copy the auto-generated SVG URLs — ready to paste into your README!



## ⚡ Deployment

Built with:

- Python 3.11+
- Flask
- Requests
- Render.com (for free hosting)
- UptimeRobot (to prevent cold starts)


## 🛠️ Setup Locally

1. Clone this repository
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file:

   ```env
   GH_TOKEN=your_github_token
   GH_USERNAME=your_github_username
   WAKA_API_KEY=your_wakatime_api_key
   ```

4. Run the app:

   ```bash
   python app.py
   ```

5. Visit `http://127.0.0.1:5000`


## 🚀 Deployment (Render.com)

1. Fork this repository
2. Go to [Render.com](https://render.com/)
3. Click **New Web Service**
4. Connect your GitHub repository
5. Fill out the following:
   - **Environment:** Python 3.11
   - **Build Command:** 
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command:** 
     ```bash
     python app.py
     ```
   - **Environment Variables:**
     - `GH_TOKEN` = your GitHub token
     - `GH_USERNAME` = your GitHub username
     - `WAKA_API_KEY` = your WakaTime API key
6. Deploy!


## 🧑‍💻 Term-Stats Query Parameters (Markdown Table)

### 🧭 Available Routes

| Route         | Description                         |
|---------------|-------------------------------------|
| `/basic`      | Displays the Basic stats.           |
| `/streaks`    | Displays the Streaks stats.         |
| `/languages`  | Displays the Languages stats.       |
| `/dev_pulse`  | Displays the Developer Pulse stats. |
| `/waka_stats` | Displays the WakaTime stats.        |
| `/distro`     | Displays the Distro stats.          |

### ✅ Query Parameters

| Parameter              | Description                                              | Example                          |
|------------------------|----------------------------------------------------------|----------------------------------|
| `username`             | GitHub username for stats generation                     | `username=YESWANTH-S`            |
| `style`                | Stats display style: `raw`, `border`, `normal`           | `style=raw`                      |
| `titleColor`           | Hex color for the title text                             | `titleColor=FFFFFF`              |
| `textColor`            | Hex color for general text                               | `textColor=CDD6F4`               |
| `valueColor`           | Hex color for values like stars or commits               | `valueColor=B4BEFE`              |
| `borderColor`          | Hex color for the border (if applicable)                 | `borderColor=CDD6F4`             |
| `backgroundColor`      | Hex color for the background (border styles only)        | `backgroundColor=FFFFFF`         |
| `gif`                  | GIF animation: `true`, `false`, `static`                 | `gif=false`                      |
| `currentStreakColor`   | Hex color for current streak                             | `currentStreakColor=B5A0F4`      |
| `quoteColor`           | Hex color for the quote (Developer Pulse section)        | `quoteColor=94E2D5`              |
| `currentMood`          | Developer's current mood                                 | `currentMood=Chill`              |
| `currentFocus`         | Current project or focus area                            | `currentFocus=Term Stats`        |
| `favoriteLanguage`     | Favorite programming language                            | `favoriteLanguage=Python`        |
| `distro`               | Operating system distribution                            | `distro=EndeavourOS`             |
| `shell`                | Shell being used                                         | `shell=zsh`                      |
| `directory`            | Current working directory                                | `directory=projects`             |


### Example URLs:

1. **Basic Stats**  
   Displays basic GitHub stats in the `raw` style and disables GIFs.
   
   Example:
   ```text
   https://term-stats.onrender.com/basic?username=YESWANTH-S&style=raw&titleColor=FFFFFF&textColor=CDD6F4&valueColor=B4BEFE&borderColor=CDD6F4&gif=false
   ```

2. **Streaks**  
   Displays contribution streak stats with custom colors.
   
   Example:
   ```text
   https://term-stats.onrender.com/streaks?username=YESWANTH-S&style=raw&titleColor=FFFFFF&textColor=CDD6F4&valueColor=B4BEFE&borderColor=CDD6F4&gif=false&currentStreakColor=B5A0F4
   ```

3. **Developer Pulse**  
   Displays personalized developer stats with mood, focus, and favorite language.

   Example:
   ```text
   https://term-stats.onrender.com/dev_pulse?username=YESWANTH-S&style=raw&titleColor=FFFFFF&textColor=CDD6F4&valueColor=B4BEFE&borderColor=CDD6F4&gif=false&quoteColor=94E2D5&currentMood=Chill&currentFocus=Term%20Stats&favoriteLanguage=Python
   ```

4. **Distro Info**  
   Displays custom OS, shell, and directory information.

   Example:
   ```text
   https://term-stats.onrender.com/distro?username=YESWANTH-S&style=raw&titleColor=FFFFFF&textColor=CDD6F4&valueColor=B4BEFE&borderColor=CDD6F4&gif=false&distro=EndeavourOS&shell=zsh&directory=projects
   ```


You can freely mix and match these query parameters to personalize your stats. Simply copy the URL with your desired parameters and embed it in your README or share it with others.


## 📝 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more information.