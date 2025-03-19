function openSec(section) {
  var secHeader, section;

  if (["photography", "projects", "about"].includes(section)) {
    secHeader = document.getElementById("section-header");
    secHeader.textContent = section.charAt(0).toUpperCase() + section.slice(1);

    window.location.hash = section;

    $("#main").fadeOut('fast', function() {
      $(`#${section}`).add("#bar").fadeIn('fast');
    });
  }
}

function closeAll() {
  var sections, currentSec;

  sections = document.getElementsByClassName("section");

  for (i = 0; i < sections.length; i++) {
    if (sections[i].checkVisibility()) {
      currentSec = sections[i];
    }
  }

  history.pushState("", document.title, window.location.pathname + window.location.search);

  $(`#${currentSec.id}`).add("#bar").fadeOut('fast', function() {
    $("#main").fadeIn('fast');
  });
}

function handleHash() {
  if (location.hash.length !== 0) {
    openSec(location.hash.substring(1));
  }
}

window.addEventListener('hashchange', handleHash());

// var prevScrollpos = window.scrollY;
// var ScrollDebounce = true;
// window.onscroll = function() {
//     if (ScrollDebounce) {
//        ScrollDebounce = false;
//
//         var currentScrollPos = window.scrollY;
//         if (prevScrollpos > currentScrollPos) {
//             document.getElementById("bar").style.top = "0";
//         } else {
//             document.getElementById("bar").style.top = "-100px";
//         }
//         prevScrollpos = currentScrollPos;
//
//         setTimeout(function () { ScrollDebounce = true; }, 500);
//     }
// }

function openPic(photoUrl, photoTitle, format, date) {
  $("#pic_large").html(`<h1>${photoTitle}</h1><h3>Taken with <span>${format}</span> &bull; Uploaded on ${date}</h3><p>click anywhere to close</p><img src=${photoUrl} alt=${photoTitle} />`);
  $("body").css("overflow", "hidden");
  $("#preview_screen").fadeIn();
}

function closePreview() {
  $("#preview_screen").fadeOut();
  $("body").css("overflow", "auto");
}