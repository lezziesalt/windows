let zIndexCounter = 1;
let desktop = document.getElementById("desktop");

// Load saved tabs on page load
window.onload = () => loadTabs();

function newWindow() {
    let input = document.getElementById("urlBox").value.trim();
    if (!input) return;
    let url = input;
    if (!input.startsWith("http://") && !input.startsWith("https://")) {
        url = "https://www.google.com/search?q=" + encodeURIComponent(input);
    }
    createWindow(url);
}

// Create a new "desktop window"
function createWindow(url, x=50, y=50) {
    let win = document.createElement("div");
    win.className = "window";
    win.style.left = x + "px";
    win.style.top = y + "px";
    win.style.zIndex = zIndexCounter++;

    // Header
    let header = document.createElement("div");
    header.className = "window-header";
    header.innerHTML = `<span>${url}</span>`;
    let closeBtn = document.createElement("button");
    closeBtn.innerText = "X";
    closeBtn.onclick = () => win.remove();
    header.appendChild(closeBtn);
    win.appendChild(header);

    // iframe
    let iframe = document.createElement("iframe");
    iframe.src = url;
    win.appendChild(iframe);

    desktop.appendChild(win);

    // Dragging
    let offsetX, offsetY;
    header.onmousedown = (e) => {
        offsetX = e.clientX - win.offsetLeft;
        offsetY = e.clientY - win.offsetTop;
        document.onmousemove = drag;
        document.onmouseup = stopDrag;
        win.style.zIndex = zIndexCounter++;
    };
    function drag(e) {
        win.style.left = e.clientX - offsetX + "px";
        win.style.top = e.clientY - offsetY + "px";
    }
    function stopDrag() {
        document.onmousemove = null;
        document.onmouseup = null;
    }
}

// Save open windows to localStorage
function saveTabs() {
    let windows = document.querySelectorAll(".window iframe");
    let urls = Array.from(windows).map(f => f.src);
    localStorage.setItem("savedTabs", JSON.stringify(urls));
    alert("Tabs saved!");
}

// Load saved windows from localStorage
function loadTabs() {
    let saved = JSON.parse(localStorage.getItem("savedTabs") || "[]");
    saved.forEach(url => createWindow(url, 60, 60));
}
