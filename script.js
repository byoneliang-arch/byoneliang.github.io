const header = document.querySelector("#siteHeader");
const navToggle = document.querySelector("#navToggle");
const navLinks = document.querySelector("#navLinks");
const navItems = document.querySelectorAll(".nav-links a");
const sections = document.querySelectorAll("main section[id]");
const revealItems = document.querySelectorAll(".reveal");
const year = document.querySelector("#year");

year.textContent = new Date().getFullYear();

function updateHeader() {
  header.classList.toggle("scrolled", window.scrollY > 24);
}

function closeMobileNav() {
  navLinks.classList.remove("open");
  navToggle.setAttribute("aria-expanded", "false");
}

navToggle.addEventListener("click", () => {
  const isOpen = navLinks.classList.toggle("open");
  navToggle.setAttribute("aria-expanded", String(isOpen));
});

navItems.forEach((item) => {
  item.addEventListener("click", closeMobileNav);
});

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        revealObserver.unobserve(entry.target);
      }
    });
  },
  {
    threshold: 0.16,
  }
);

revealItems.forEach((item) => revealObserver.observe(item));

const sectionObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;

      navItems.forEach((item) => {
        const isActive = item.getAttribute("href") === `#${entry.target.id}`;
        item.classList.toggle("active", isActive);
      });
    });
  },
  {
    rootMargin: "-45% 0px -45% 0px",
  }
);

sections.forEach((section) => sectionObserver.observe(section));

window.addEventListener("scroll", updateHeader, { passive: true });
window.addEventListener("resize", () => {
  if (window.innerWidth > 720) closeMobileNav();
});

updateHeader();
