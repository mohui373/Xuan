/* Site-local progressive enhancement. All content stays visible without JavaScript. */
(() => {
  const root = document.querySelector(".research-motion");
  if (!root || root.dataset.motionInitialized) return;
  root.dataset.motionInitialized = "true";

  const preference = window.matchMedia("(prefers-reduced-motion: reduce)");
  const connection = navigator.connection;
  const lowData = connection?.saveData || /(^|-)2g$/.test(connection?.effectiveType || "");
  if (preference.matches || lowData || !window.IntersectionObserver || !Element.prototype.animate) return;

  const running = new Set();
  const pending = new Set();
  const play = (element, index) => {
    if (preference.matches || document.hidden || element.matches(":focus-within")) return;
    const animation = element.animate(
      [
        { opacity: 0.45, transform: "translateY(10px)" },
        { opacity: 1, transform: "translateY(0)" },
      ],
      { duration: 420, delay: Math.min(index, 2) * 40, easing: "cubic-bezier(0.22, 1, 0.36, 1)" }
    );
    running.add(animation);
    animation.addEventListener("finish", () => running.delete(animation), { once: true });
    animation.addEventListener("cancel", () => running.delete(animation), { once: true });
  };

  const observer = new IntersectionObserver(
    (entries) => {
      let index = 0;
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        observer.unobserve(entry.target);
        pending.delete(entry.target);
        play(entry.target, index++);
      }
      if (!pending.size) observer.disconnect();
    },
    { threshold: 0.12 }
  );

  // Never animate the initial viewport: no delayed hero text, portrait, or LCP candidate.
  const candidates = root.querySelectorAll(".research-question-band, .stream-row, .research-detail-header, .research-detail-grid > div");
  for (const element of candidates) {
    if (element.getBoundingClientRect().top <= window.innerHeight + 24) continue;
    pending.add(element);
    observer.observe(element);
  }

  const stop = () => {
    observer.disconnect();
    pending.clear();
    for (const animation of running) animation.cancel();
    running.clear();
  };
  preference.addEventListener("change", (event) => {
    if (event.matches) stop();
  });
  root.addEventListener("focusin", () => {
    for (const animation of running) animation.cancel();
    running.clear();
  });
  document.addEventListener("visibilitychange", () => {
    if (!document.hidden) return;
    for (const animation of running) animation.cancel();
    running.clear();
  });
  window.addEventListener("pagehide", stop, { once: true });
})();
