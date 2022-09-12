if(typeof window.IntersectionObserver !== 'undefined') {
  let options = {
    threshold: [0.5, 1]
  }
  const targets = document.querySelectorAll('.cb');
  const locker = document.querySelector('.locker__container');
  function handleIntersection(entries) {
    entries.map((entry) => {
      if (entry.isIntersecting) {
        entry.target.current = entry.target.dataset.swap;
        document.querySelector(".locker__container ." + entry.target.current).classList.add("active");
      } else {
        document.querySelector(".locker__container ." + entry.target.current).classList.remove("active");
      }
    });
  }
  const observer = new IntersectionObserver(handleIntersection, options);
  targets.forEach(target => observer.observe(target));
} else {
  // Fallback
}