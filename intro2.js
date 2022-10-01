var intro = introJs().setOptions({
    hidePrev: true,
    hideNext: true,
    exitOnOverlayClick: false,
    exitOnEsc: false,
    steps: [
      {
        element: document.querySelector("#principal"),
        intro: "This is the principal."
      },
      {
        element: document.querySelector("#tenor"),
        intro: "This is the tenor"
      },
      {
        element: document.querySelector("#acceptordeny"),
        intro:
          "<p>This is a button that needs a good clicking</p>",
           tooltipClass: "wideo"
      }
    ]
  }).oncomplete(() => document.cookie = "intros-complete=true");
  
  var start = () => intro.start();
  
  window.addEventListener("load", () =>
    document.querySelector("#starter").addEventListener("click", e => {
      e.preventDefault();
      start();
    })
  );
  
  if (document.cookie.split(";").indexOf("intros-complete=true") < 0)
    window.setTimeout(start, 1000);