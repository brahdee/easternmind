function openTab(tabId) {
    var previousTab = document.getElementsByClassName("active").item(0);
    previousTab.classList.remove("active");

    var previousTabContent = document.getElementsByClassName("shown").item(0);
    previousTabContent.classList.remove("shown");
    previousTabContent.classList.add("hidden");

    var tabPressed = document.getElementById(tabId + "-btn");
    tabPressed.classList.add("active");

    var contentToShow = document.getElementById(tabId);
    contentToShow.classList.remove("hidden");
    contentToShow.classList.add("shown");
}

function toggleFullscreen() {
    if (this.fullscreenElement) {
        this.exitFullscreeen;
    } else {
        this.requestFullscreen;
    }
}