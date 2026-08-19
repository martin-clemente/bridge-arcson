document.addEventListener("DOMContentLoaded", function () {
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var isOpen = nav.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
  }

  var counters = document.querySelectorAll(".num[data-target]");
  counters.forEach(function (el) {
    var target = parseInt(el.getAttribute("data-target"), 10);
    var prefix = el.getAttribute("data-prefix") || "";
    var suffix = el.getAttribute("data-suffix") || "";
    var duration = 2000;
    var start = null;

    function step(ts) {
      if (!start) start = ts;
      var progress = Math.min((ts - start) / duration, 1);
      var current = Math.floor(progress * target);
      el.textContent = prefix + current + suffix;
      if (progress < 1) requestAnimationFrame(step);
    }

    setTimeout(function () { requestAnimationFrame(step); }, 800);
  });

  document.querySelectorAll(".vision-item h3").forEach(function (h3) {
    var text = h3.textContent;
    h3.innerHTML = "";
    text.split("").forEach(function (ch, i) {
      var span = document.createElement("span");
      span.className = "letter";
      span.textContent = ch === " " ? "\u00a0" : ch;
      span.style.transitionDelay = (i * 35) + "ms";
      h3.appendChild(span);
    });
  });

  if ("IntersectionObserver" in window) {
    var animated = document.querySelectorAll("[data-animate]");
    if (animated.length) {
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            var items = entry.target.querySelectorAll(".vision-item");
            items.forEach(function (item, i) {
              setTimeout(function () { item.classList.add("is-visible"); }, i * 180);
            });
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.2 });
      var row = document.querySelector(".vision-row");
      if (row) observer.observe(row);
    }

    var revealTexts = document.querySelectorAll(".reveal-text");
    if (revealTexts.length) {
      var headObs = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            headObs.unobserve(entry.target);
          }
        });
      }, { threshold: 0.3 });
      revealTexts.forEach(function (el) { headObs.observe(el); });
    }

    var cards = document.querySelectorAll(".component-card");
    if (cards.length) {
      var cardObs = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            cardObs.unobserve(entry.target);
          }
        });
      }, { threshold: 0.15 });
      cards.forEach(function (el, i) {
        el.style.transitionDelay = (i * 150) + "ms";
        cardObs.observe(el);
      });
    }

    var scrollAnims = document.querySelectorAll(".animate-on-scroll");
    if (scrollAnims.length) {
      var scrollObs = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            scrollObs.unobserve(entry.target);
          }
        });
      }, { threshold: 0.2 });
      scrollAnims.forEach(function (el, i) {
        el.style.transitionDelay = (i * 180) + "ms";
        scrollObs.observe(el);
      });
    }
  } else {
    document.querySelectorAll(".vision-item, .component-card, .reveal-text, .animate-on-scroll").forEach(function (el) {
      el.classList.add("is-visible");
    });
  }
});
