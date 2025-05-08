// Default colors for Pickr
const pickrColors = {
    titleColor: '#ffffff',
    textColor: '#cdd6f4',
    valueColor: '#b4befe',
    borderColor: '#cdd6f4',
    currentStreakColor: '#b5a0f4',
    quoteColor: '#94e2d5',
    backgroundColor: '#00000000'
};

const pickrs = {};

// Create Pickr instances
function createPickr(id) {
    const stored = localStorage.getItem(id);
    const defaultColor = stored || pickrColors[id];

    pickrs[id] = Pickr.create({
        el: `#${id}Dot`,
        useAsButton: true,
        theme: 'nano',
        swatches: [
        'rgba(244, 67, 54, 1)',
        'rgba(233, 30, 99, 1)',
        'rgba(156, 39, 176, 1)',
        'rgba(103, 58, 183, 1)',
        'rgba(63, 81, 181, 1)',
        'rgba(33, 150, 243, 1)',
        'rgba(3, 169, 244, 1)',
        'rgba(0, 188, 212, 1)',
        'rgba(0, 150, 136, 1)',
        'rgba(76, 175, 80, 1)',
        'rgba(139, 195, 74, 1)',
        'rgba(205, 220, 57, 1)',
        'rgba(255, 235, 59, 1)',
        'rgba(255, 193, 7, 1)',
        ],
        default: defaultColor,
        components: {
            preview: true,
            opacity: true,
            hue: true,
            interaction: {
                hex: true,
                input: true,
                save: true
            }
        }
    });

    pickrs[id].on('save', (color) => {
        const hex = color.toHEXA().toString();
        document.getElementById(`${id}Dot`).style.backgroundColor = hex;
        localStorage.setItem(id, hex);
        pickrs[id].hide(); // Optional: auto-close on save
    });

    document.getElementById(`${id}Dot`).style.backgroundColor = defaultColor;
}

// Initialize all Pickr color pickers
function initializePickrs() {
    [
        'titleColor',
        'textColor',
        'valueColor',
        'borderColor',
        'currentStreakColor',
        'quoteColor',
        'backgroundColor'
    ].forEach(createPickr);
}

// Apply customization and generate URL
function applyCustomization() {
    const svg = document.getElementById('svgObject');
    const container = document.getElementById('svgContainer');
    const timestamp = new Date().getTime();

    function showSectionWarning(id) {
        const warning = document.getElementById(id);
        if (!warning) return;
    
        warning.style.display = "block";
        warning.style.opacity = "1";
        setTimeout(() => {
            warning.style.opacity = "0";
            setTimeout(() => {
                warning.style.display = "none";
                warning.style.opacity = "1";
            }, 500);
        }, 3000);
    }
    
    const username = document.getElementById("usernameInput").value.trim();
    const usernameRegex = /^(?!-)(?!.*--)[a-zA-Z0-9-]{1,39}(?<!-)$/;
    
    if (!username) {
        showSectionWarning("usernameWarning");
        return;
    }
    
    if (!usernameRegex.test(username)) {
        document.getElementById("usernameWarning").textContent = "[!] Invalid GitHub username.";
        showSectionWarning("usernameWarning");
        return;
    } else {
        document.getElementById("usernameWarning").textContent = "[!] Please enter a GitHub username.";
    }
    
if (document.getElementById("distroFields").style.display !== "none") {
    const distro = document.getElementById("distroInput").value.trim();
    const shell = document.getElementById("shellInput").value.trim();
    const directory = document.getElementById("directoryInput").value.trim();
    if (!distro || !shell || !directory) {
        showSectionWarning("distroWarning");
        return;
    }
}

if (document.getElementById("devPulseFields").style.display !== "none") {
    const mood = document.getElementById("currentMoodInput").value.trim();
    const focus = document.getElementById("currentFocusInput").value.trim();
    const lang = document.getElementById("favoriteLanguageInput").value.trim();
    if (!mood || !focus || !lang) {
        showSectionWarning("devPulseWarning");
        return;
    }
}

    const style = document.getElementById("styleSelect").value;
    const titleColor = pickrs['titleColor'].getColor().toHEXA().toString().substring(1);
    const textColor = pickrs['textColor'].getColor().toHEXA().toString().substring(1);
    const valueColor = pickrs['valueColor'].getColor().toHEXA().toString().substring(1);
    const borderColor = pickrs['borderColor'].getColor().toHEXA().toString().substring(1);
    const backgroundColor = pickrs['backgroundColor'].getColor().toHEXA().toString().substring(1);
    const gif = document.getElementById("gifSelect").value;

    const activeButton = document.querySelector('.sidebar button.active');
    const currentPath = activeButton ? activeButton.getAttribute('onclick').match(/'(.*?)'/)[1] : 'basic?style=raw';
    const statType = currentPath.split('?')[0];

    let url = `/${statType}?style=${style}&titleColor=${titleColor}&textColor=${textColor}&valueColor=${valueColor}&borderColor=${borderColor}&backgroundColor=${backgroundColor}&gif=${gif}&t=${timestamp}`;

    if (statType !== 'waka_stats') {
        url = `/${statType}?username=${encodeURIComponent(username)}&style=${style}&titleColor=${titleColor}&textColor=${textColor}&valueColor=${valueColor}&borderColor=${borderColor}&backgroundColor=${backgroundColor}&gif=${gif}&t=${timestamp}`;
    }

    if (statType === "streaks") {
        const currentStreakColor = pickrs['currentStreakColor'].getColor().toHEXA().toString().substring(1);
        url += `&currentStreakColor=${currentStreakColor}`;
        localStorage.setItem('currentStreakColor', `#${currentStreakColor}`);
    }

    if (statType === "dev_pulse") {
        const quoteColor = pickrs['quoteColor'].getColor().toHEXA().toString().substring(1);
        url += `&quoteColor=${quoteColor}`;
        localStorage.setItem('quoteColor', `#${quoteColor}`);

        const currentMood = document.getElementById("currentMoodInput").value.trim();
        const currentFocus = document.getElementById("currentFocusInput").value.trim();
        const favoriteLanguage = document.getElementById("favoriteLanguageInput").value.trim();

        if (currentMood && currentFocus && favoriteLanguage) {
            url += `&currentMood=${encodeURIComponent(currentMood)}&currentFocus=${encodeURIComponent(currentFocus)}&favoriteLanguage=${encodeURIComponent(favoriteLanguage)}`;
        }
    }

    if (statType === 'distro') {
        const distro = document.getElementById("distroInput").value.trim();
        const shell = document.getElementById("shellInput").value.trim();
        const directory = document.getElementById("directoryInput").value.trim();
        if (distro && shell && directory) {
            url += `&distro=${encodeURIComponent(distro)}&shell=${encodeURIComponent(shell)}&directory=${encodeURIComponent(directory)}`;
        }
    }

    svg.data = url;
    container.style.width = '600px';
    container.style.height = '200px';
    container.style.border = '2px solid #cdd6f4';

    // Save to localStorage
    localStorage.setItem('titleColor', `#${titleColor}`);
    localStorage.setItem('textColor', `#${textColor}`);
    localStorage.setItem('valueColor', `#${valueColor}`);
    localStorage.setItem('borderColor', `#${borderColor}`);
    localStorage.setItem('backgroundColor', `#${backgroundColor}`);

    document.getElementById('generatedUrl').value = url;
    document.getElementById('urlDisplayGroup').style.display = 'flex';
}

// Copy generated URL to clipboard
function copyUrl(event) {
    const urlField = document.getElementById("generatedUrl");
    const baseUrl = "http://127.0.0.1:5000";
    const fullUrl = baseUrl + urlField.value;

    navigator.clipboard.writeText(fullUrl).then(() => {
        const icon = event.target.querySelector('i');
        const originalIconClass = icon.className;
        icon.className = "fas fa-check";

        setTimeout(() => {
            icon.className = originalIconClass;
        }, 1000);
    }).catch(err => {
        console.error("Failed to copy: ", err);
    });
}

// Load SVG based on selection
function loadSVG(type, buttonElement) {
    const svg = document.getElementById('svgObject');
    const container = document.getElementById('svgContainer');
    const timestamp = new Date().getTime();
    const statType = type.split('?')[0];

    svg.data = `/${type}${type.includes('?') ? '&' : '?'}t=${timestamp}`;

    const buttons = document.querySelectorAll('.sidebar button');
    buttons.forEach(btn => btn.classList.remove('active'));
    buttonElement.classList.add('active');

    const streakGroup = document.getElementById('streakColorGroup');
    const quoteGroup = document.getElementById('quoteColorGroup');
    const optionsContainer = document.getElementById('optionsContainer');
    const wakaInstructions = document.getElementById('wakaInstructions');
    const distroFields = document.getElementById('distroFields');
    const devPulseFields = document.getElementById('devPulseFields');
    const usernameGroup = document.getElementById('usernameInput').closest('.option-group');

    streakGroup.style.display = (statType === 'streaks') ? 'flex' : 'none';
    quoteGroup.style.display = (statType === 'dev_pulse') ? 'flex' : 'none';

    distroFields.style.display = (statType === 'distro') ? 'flex' : 'none';
    devPulseFields.style.display = (statType === 'dev_pulse') ? 'flex' : 'none';
    usernameGroup.style.display = (statType === 'waka_stats') ? 'none' : 'block';
}

// Initialize everything on page load
window.onload = () => {
    initializePickrs();
    const firstButton = document.querySelector('.sidebar button');
    loadSVG('basic?style=raw', firstButton);
};
