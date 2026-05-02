const navbar = document.getElementById("navbar");

window.addEventListener("scroll", () => {
  if (window.scrollY > 60) {
    navbar.classList.add("scrolled");
  } else {
    navbar.classList.remove("scrolled");
  }

  highlightActiveNav();
});

function highlightActiveNav() {
  const sections = document.querySelectorAll("section[id]");
  const navLinks  = document.querySelectorAll(".nav-link");

  let currentSection = "";

  sections.forEach((section) => {
    if (window.scrollY >= section.offsetTop - 200) {
      currentSection = section.getAttribute("id");
    }
  });

  navLinks.forEach((link) => {
    link.classList.remove("active");
    if (link.getAttribute("href") === `#${currentSection}`) {
      link.classList.add("active");
    }
  });
}

const typingElement = document.getElementById("typingText");
const phrases = [
  "MCA Graduate",
  "Full Stack Developer",
  "Python Enthusiast",
  "Problem Solver",
  "Quick Learner"
];

let phraseIndex = 0;
let charIndex   = 0;
let isDeleting  = false;

function typeEffect() {
  const currentPhrase = phrases[phraseIndex];

  if (isDeleting) {
    typingElement.textContent = currentPhrase.substring(0, charIndex - 1);
    charIndex--;
  } else {
    typingElement.textContent = currentPhrase.substring(0, charIndex + 1);
    charIndex++;
  }

  let speed = isDeleting ? 60 : 110;

  if (!isDeleting && charIndex === currentPhrase.length) {
    speed = 2000;
    isDeleting = true;
  } else if (isDeleting && charIndex === 0) {
    isDeleting = false;
    phraseIndex = (phraseIndex + 1) % phrases.length;
    speed = 400;
  }

  setTimeout(typeEffect, speed);
}

setTimeout(typeEffect, 800);

async function loadProjects() {
  const grid    = document.getElementById("projectsGrid");
  const loading = document.getElementById("projectsLoading");

  try {
    const response = await fetch("/api/projects");
    const data     = await response.json();

    if (!data.success || !data.projects.length) {
      grid.innerHTML = "<p style='color:var(--muted);text-align:center;grid-column:1/-1'>No projects found.</p>";
      return;
    }

    loading.remove();

    data.projects.forEach((project, index) => {
      const card = buildProjectCard(project, index);
      grid.appendChild(card);
    });

    observeReveal();

  } catch (error) {
    console.error("Failed to load projects:", error);
    loading.innerHTML = "<p style='color:var(--error);text-align:center'>Could not load projects. Make sure Flask is running.</p>";
  }
}

function buildProjectCard(p, index) {
  const card = document.createElement("div");
  card.className = "project-card reveal";
  card.style.animationDelay = `${index * 0.1}s`;

  const featuresHTML = p.features
    .map(f => `<li>${f}</li>`)
    .join("");

  const techHTML = p.tech_stack
    .map(t => `<span class="tech-pill">${t}</span>`)
    .join("");

  card.innerHTML = `
    <div class="project-header">
      <span class="project-emoji">${p.emoji}</span>
      <span class="project-category">${p.category}</span>
    </div>

    <h3 class="project-title">${p.title}</h3>
    <p class="project-tagline">${p.tagline}</p>

    <p class="project-desc">${p.description}</p>

    <div class="project-use">
      <strong>💡 Real-World Use Case</strong>
      ${p.real_world_use}
    </div>

    <ul class="project-features">
      ${featuresHTML}
    </ul>

    <div class="project-tech">
      ${techHTML}
    </div>

    <div class="project-actions">
      <a href="${p.github}" target="_blank" class="btn btn-outline">GitHub ↗</a>
      <a href="${p.demo}"   target="_blank" class="btn btn-primary">Live Demo ↗</a>
    </div>
  `;

  return card;
}

document.addEventListener("DOMContentLoaded", loadProjects);

const contactForm = document.getElementById("contactForm");
const submitBtn   = document.getElementById("submitBtn");
const feedback    = document.getElementById("formFeedback");

contactForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const formData = {
    name:    document.getElementById("name").value.trim(),
    email:   document.getElementById("email").value.trim(),
    subject: document.getElementById("subject").value.trim(),
    message: document.getElementById("message").value.trim(),
  };

  submitBtn.textContent = "Sending...";
  submitBtn.disabled    = true;

  feedback.className = "form-feedback";
  feedback.textContent = "";

  try {
    const response = await fetch("/api/contact", {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify(formData),
    });

    const result = await response.json();

    if (result.success) {
      feedback.className   = "form-feedback success";
      feedback.textContent = result.message;
      contactForm.reset();
    } else {
      feedback.className   = "form-feedback error";
      feedback.textContent = result.error || "Something went wrong.";
    }

  } catch (error) {
    feedback.className   = "form-feedback error";
    feedback.textContent = "Network error — please try again.";
  }

  submitBtn.textContent = "Send Message 🚀";
  submitBtn.disabled    = false;
});

function observeReveal() {
  const revealElements = document.querySelectorAll(".reveal");

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1 }
  );

  revealElements.forEach((el) => observer.observe(el));
}

document.addEventListener("DOMContentLoaded", observeReveal);

const hamburger = document.getElementById("hamburger");
const navLinks  = document.getElementById("navLinks");

hamburger.addEventListener("click", () => {
  navLinks.classList.toggle("open");
});

document.querySelectorAll(".nav-link").forEach((link) => {
  link.addEventListener("click", () => {
    navLinks.classList.remove("open");
  });
});

document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    const targetId = this.getAttribute("href");
    if (targetId === "#") return;

    const target = document.querySelector(targetId);
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  });
});