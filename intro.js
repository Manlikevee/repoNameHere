var intro = introJs().setOptions({
    hidePrev: true,
    hideNext: true,
    exitOnOverlayClick: false,
    exitOnEsc: false,
    steps: [
      {
        element: document.querySelector("#investmentblock"),
        intro: "This whole area does something."
      },
      {
        element: document.querySelector("#download"),
        intro: "This is the first item in the list. It also does something."
      },
      {
        element: document.querySelector("#tabsli"),
        intro: "This second item probably does something as well"
      },
      {
        element: document.querySelector("#headme"),
        intro: "This second is where the header is"
      },
      {
        element: document.querySelector("#invsamp"),
        intro:
          "<p>This is a button that needs a good clicking</p>",
           tooltipClass: "wideo"
      }
    ]
  }).oncomplete(() => document.cookie = "intro-complete=true");
  
  var start = () => intro.start();
  
  window.addEventListener("load", () =>
    document.querySelector("#starter").addEventListener("click", e => {
      e.preventDefault();
      start();
    })
  );
  
  if (document.cookie.split(";").indexOf("intro-complete=true") < 0)
    window.setTimeout(start, 1000);