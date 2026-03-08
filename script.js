let zIndexCounter = 1;
let desktop = document.getElementById("desktop");

// Button click works now
document.getElementById("openBtn").addEventListener("click", () => {
    let input = document.getElementById("urlBox").value.trim();
    if (!input) return;

    // Add https:// if missing
    let url = input;
    if (!input.startsWith("http://") && !input.startsWith("https://")) {
        url = "https://en.wikipedia.org/wiki/" + encodeURIComponent(input);
    }

    openWindow(url);
});

function openWindow(url, x=50, y=50) {
    let win = document.createElement("div");
    win.className = "window";
    win.style.left = x + "px";
    win.style.top = y + "px";
    win.style.zIndex = zIndexCounter++;

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
