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

var pastThreshold = false;

$(window).scroll(function() {
  var $w = $(window);

  $('#main-text').each(function() {
    $(this).css('opacity', (1 - $w.scrollTop() / 300));
    $(this).css('transform', `translate(-50%, -${(50 + ($w.scrollTop() / 100))}%)`);
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const observerOptions = {
    root: null,
    rootMargin: "0px",
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("now-visible");
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  const hiddenElements = document.querySelectorAll(".temp-hidden");
  hiddenElements.forEach(el => observer.observe(el));
});