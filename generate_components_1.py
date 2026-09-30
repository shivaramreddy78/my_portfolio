import os

base_dir = "/Users/shivaramreddy/projects/protfolio"

files = {
"src/components/Navbar.jsx": """import React, { useState, useEffect } from 'react';
import { ArrowUpRight } from './icons';

const Navbar = () => {
  const [scrolled, setScrolled] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <header className={`navbar-wrapper ${scrolled ? 'scrolled' : ''}`}>
      <nav className="navbar">
        <div className="nav-brand">SHIVARAM REDDY</div>
        
        <div className="nav-links desktop-only">
          <a href="#home">Home</a>
          <a href="#about">About</a>
          <a href="#capabilities">Capabilities</a>
          <a href="#projects">Projects</a>
          <a href="#experience">Experience</a>
          <a href="#contact">Contact</a>
        </div>

        <div className="nav-cta desktop-only">
          <a href="#contact" className="pill-button">
            Let's Talk <ArrowUpRight />
          </a>
        </div>

        <button 
          className="mobile-menu-toggle mobile-only"
          onClick={() => setMenuOpen(!menuOpen)}
          aria-label="Toggle menu"
        >
          ☰
        </button>
      </nav>

      {menuOpen && (
        <div className="mobile-menu">
          <a href="#home" onClick={() => setMenuOpen(false)}>Home</a>
          <a href="#about" onClick={() => setMenuOpen(false)}>About</a>
          <a href="#capabilities" onClick={() => setMenuOpen(false)}>Capabilities</a>
          <a href="#projects" onClick={() => setMenuOpen(false)}>Projects</a>
          <a href="#experience" onClick={() => setMenuOpen(false)}>Experience</a>
          <a href="#contact" onClick={() => setMenuOpen(false)}>Contact</a>
          <a href="#contact" className="pill-button" onClick={() => setMenuOpen(false)}>
            Let's Talk <ArrowUpRight />
          </a>
        </div>
      )}
    </header>
  );
};

export default Navbar;
""",

"src/components/Navbar.css": """
.navbar-wrapper {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  padding: 1.5rem 5%;
  z-index: 100;
  transition: all 0.4s ease;
  pointer-events: none;
}

.navbar-wrapper.scrolled {
  padding: 1rem 5%;
}

.navbar {
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  pointer-events: auto;
  background: var(--glass);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--glass-border);
  border-radius: 99px;
  padding: 0.5rem 0.5rem 0.5rem 2rem;
  transition: all 0.4s ease;
}

.nav-brand {
  font-family: var(--font-display);
  font-weight: 600;
  font-size: 1rem;
  letter-spacing: 0.05em;
}

.nav-links {
  display: flex;
  gap: 2.5rem;
}

.nav-links a {
  font-size: 0.9rem;
  color: var(--ink-soft);
  transition: color 0.3s ease;
}

.nav-links a:hover {
  color: var(--ink);
}

.mobile-only {
  display: none;
}

.mobile-menu-toggle {
  background: none;
  border: none;
  color: var(--ink);
  font-size: 1.5rem;
  cursor: pointer;
  padding: 0.5rem 1rem;
}

.mobile-menu {
  position: absolute;
  top: 100%;
  left: 5%;
  right: 5%;
  margin-top: 1rem;
  background: rgba(22, 7, 3, 0.95);
  backdrop-filter: blur(20px);
  border: 1px solid var(--glass-border);
  border-radius: 24px;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  pointer-events: auto;
  animation: slideDown 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.mobile-menu a {
  font-size: 1.2rem;
  color: var(--ink-soft);
  text-decoration: none;
}

.mobile-menu a:hover {
  color: var(--ink);
}

@keyframes slideDown {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 940px) {
  .desktop-only { display: none !important; }
  .mobile-only { display: block; }
  .navbar { padding: 0.8rem 1.5rem; }
}
""",

"src/components/Hero.jsx": """import React from 'react';
import { ArrowRight, ArrowUpRight, ArrowDown } from './icons';

const Hero = () => {
  return (
    <section id="home" className="hero-section">
      <div className="hero-background">
        <div className="glow glow-1"></div>
        <div className="glow glow-2"></div>
        <div className="grain-overlay"></div>
      </div>
      
      <div className="hero-content">
        <div className="hero-eyebrow animate-rise">
          FULL STACK DEVELOPER · AI · WEB TECHNOLOGY
        </div>
        
        <h1 className="hero-title animate-rise delay-1">
          Building<br />
          Digital Experiences<br />
          with <span className="italic-accent">Intelligence.</span>
        </h1>
        
        <p className="hero-description animate-rise delay-2">
          I build modern web applications, AI-powered products and<br />
          practical digital experiences that turn ideas into working software.
        </p>
        
        <div className="hero-actions animate-rise delay-3">
          <a href="#projects" className="pill-button primary">
            View My Work <ArrowRight />
          </a>
          <a href="#contact" className="pill-button">
            Let's Connect <ArrowUpRight />
          </a>
        </div>
      </div>

      <div className="hero-proof-elements animate-rise delay-4">
        <div className="floating-labels">
          <span className="proof-label">AI</span>
          <span className="proof-label">WEB</span>
          <span className="proof-label">API</span>
          <span className="proof-label">CLOUD</span>
        </div>
        
        <div className="proof-cards">
          <div className="glass-card">
            <h4>FULL STACK</h4>
            <p>Modern frontend + backend<br/>applications</p>
          </div>
          <div className="glass-card">
            <h4>AI PROJECTS</h4>
            <p>Computer Vision<br/>Generative AI<br/>Intelligent Systems</p>
          </div>
        </div>
      </div>

      <div className="ghost-panel animate-rise delay-5">
        BUILDING REAL PRODUCTS<br/>
        AI · WEB · API · CLOUD
      </div>

      <div className="scroll-indicator animate-rise delay-5">
        <span>SCROLL TO EXPLORE</span>
        <ArrowDown />
      </div>
    </section>
  );
};

export default Hero;
""",

"src/components/Hero.css": """
.hero-section {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: 8rem 5% 4rem;
  overflow: hidden;
  border-bottom: 1px solid var(--glass-border);
}

.hero-background {
  position: absolute;
  inset: 0;
  z-index: 0;
  background: var(--ground-deep);
}

.glow {
  position: absolute;
  border-radius: 50%;
  filter: blur(100px);
  opacity: 0.15;
  animation: float 20s infinite alternate ease-in-out;
}

.glow-1 {
  top: 10%;
  left: 20%;
  width: 60vw;
  height: 60vw;
  background: radial-gradient(circle, var(--flame) 0%, transparent 70%);
}

.glow-2 {
  bottom: 0;
  right: 10%;
  width: 50vw;
  height: 50vw;
  background: radial-gradient(circle, var(--flame-lit) 0%, transparent 70%);
  animation-delay: -10s;
}

.grain-overlay {
  position: absolute;
  inset: 0;
  opacity: 0.03;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
}

.hero-content {
  position: relative;
  z-index: 2;
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
}

.hero-eyebrow {
  font-family: var(--font-body);
  font-size: 0.75rem;
  letter-spacing: 0.15em;
  color: var(--flame-lit);
  margin-bottom: 2rem;
  display: inline-block;
  padding: 0.4rem 1rem;
  border: 1px solid var(--glass-border);
  border-radius: 99px;
  background: var(--glass);
}

.hero-title {
  font-size: clamp(3.5rem, 8vw, 6.5rem);
  font-weight: 500;
  line-height: 1.05;
  margin-bottom: 2.5rem;
  color: var(--ink);
}

.italic-accent {
  font-family: var(--font-accent);
  font-style: italic;
  font-weight: 400;
  color: var(--ink-soft);
}

.hero-description {
  font-size: clamp(1.1rem, 2vw, 1.4rem);
  color: var(--ink-faint);
  max-width: 700px;
  margin-bottom: 3rem;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.hero-proof-elements {
  position: absolute;
  right: 5%;
  bottom: 10%;
  z-index: 2;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  align-items: flex-end;
}

.floating-labels {
  display: flex;
  gap: 0.8rem;
}

.proof-label {
  font-size: 0.7rem;
  letter-spacing: 0.1em;
  padding: 0.3rem 0.8rem;
  border-radius: 4px;
  background: var(--glass);
  border: 1px solid var(--glass-border);
  color: var(--ink-soft);
}

.proof-cards {
  display: flex;
  gap: 1rem;
}

.glass-card {
  background: var(--glass);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid var(--glass-border);
  padding: 1.5rem;
  border-radius: 16px;
  text-align: left;
  min-width: 180px;
}

.glass-card h4 {
  font-size: 0.8rem;
  letter-spacing: 0.1em;
  color: var(--ink-soft);
  margin-bottom: 0.8rem;
}

.glass-card p {
  font-size: 0.85rem;
  color: var(--ink-faint);
  line-height: 1.4;
}

.ghost-panel {
  position: absolute;
  left: 5%;
  top: 50%;
  transform: translateY(-50%);
  font-family: var(--font-display);
  font-size: 6rem;
  line-height: 0.9;
  font-weight: 700;
  color: var(--ink-ghost);
  opacity: 0.03;
  z-index: 1;
  pointer-events: none;
  white-space: nowrap;
}

.scroll-indicator {
  position: absolute;
  bottom: 2rem;
  left: 5%;
  z-index: 2;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.7rem;
  letter-spacing: 0.1em;
  color: var(--ink-faint);
}

.scroll-indicator svg {
  animation: bounce 2s infinite;
}

@keyframes rise {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-rise {
  opacity: 0;
  animation: rise 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.delay-1 { animation-delay: 0.2s; }
.delay-2 { animation-delay: 0.4s; }
.delay-3 { animation-delay: 0.6s; }
.delay-4 { animation-delay: 0.8s; }
.delay-5 { animation-delay: 1s; }

@keyframes float {
  0% { transform: translate(0, 0); }
  50% { transform: translate(30px, -30px); }
  100% { transform: translate(-20px, 20px); }
}

@keyframes bounce {
  0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
  40% { transform: translateY(5px); }
  60% { transform: translateY(3px); }
}

@media (max-width: 1119px) {
  .hero-proof-elements {
    position: relative;
    right: auto;
    bottom: auto;
    align-items: flex-start;
    margin-top: 4rem;
  }
  .ghost-panel {
    display: none;
  }
}

@media (max-width: 768px) {
  .hero-section {
    padding-top: 10rem;
  }
  .proof-cards {
    flex-direction: column;
    width: 100%;
  }
  .glass-card {
    width: 100%;
  }
}
""",

"src/components/About.jsx": """import React, { useEffect, useRef } from 'react';
import { portfolioData } from '../data/portfolio';

const About = () => {
  const sectionRef = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      },
      { threshold: 0.2 }
    );

    if (sectionRef.current) {
      observer.observe(sectionRef.current);
    }

    return () => {
      if (sectionRef.current) {
        observer.unobserve(sectionRef.current);
      }
    };
  }, []);

  return (
    <section id="about" className="section about-section" ref={sectionRef}>
      <div className="section-label">01 — ABOUT</div>
      
      <div className="about-grid">
        <div className="about-content">
          <h2 className="section-heading">
            I build with curiosity,<br />
            <span className="italic-accent">code with purpose.</span>
          </h2>
          <div className="about-text">
            <p>{portfolioData.about.description1}</p>
            <p>{portfolioData.about.description2}</p>
          </div>
        </div>
        
        <div className="about-visual">
          <div className="visual-composition">
            <div className="math-element">CODE</div>
            <div className="math-operator">+</div>
            <div className="math-element">AI</div>
            <div className="math-operator">+</div>
            <div className="math-element">WEB</div>
            <div className="math-operator">+</div>
            <div className="math-element">IDEAS</div>
            <div className="math-operator">=</div>
            <div className="math-result">PRODUCTS</div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;
""",

"src/components/About.css": """
.about-section {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 1s ease, transform 1s ease;
}

.about-section.visible {
  opacity: 1;
  transform: translateY(0);
}

.about-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
}

.about-text {
  font-size: 1.1rem;
  color: var(--ink-soft);
  max-width: 600px;
}

.about-text p {
  margin-bottom: 1.5rem;
}

.about-visual {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  min-height: 400px;
  background: var(--glass);
  border: 1px solid var(--glass-border);
  border-radius: 24px;
  padding: 4rem;
  position: relative;
  overflow: hidden;
}

.about-visual::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at center, rgba(255,255,255,0.03) 0%, transparent 70%);
}

.visual-composition {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  font-family: var(--font-display);
  font-size: 2rem;
  font-weight: 500;
  color: var(--ink-soft);
}

.math-element {
  letter-spacing: 0.2em;
}

.math-operator {
  color: var(--flame);
  font-weight: 300;
}

.math-result {
  color: var(--ink);
  font-size: 2.5rem;
  letter-spacing: 0.1em;
  margin-top: 1rem;
  position: relative;
}

.math-result::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 0;
  width: 100%;
  height: 2px;
  background: var(--flame);
}

@media (max-width: 940px) {
  .about-grid {
    grid-template-columns: 1fr;
  }
  .about-visual {
    min-height: 300px;
    padding: 2rem;
  }
}
""",

"src/components/Skills.jsx": """import React, { useEffect, useRef } from 'react';
import { portfolioData } from '../data/portfolio';

const Skills = () => {
  const sectionRef = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      },
      { threshold: 0.1 }
    );

    if (sectionRef.current) {
      observer.observe(sectionRef.current);
    }

    return () => {
      if (sectionRef.current) {
        observer.unobserve(sectionRef.current);
      }
    };
  }, []);

  return (
    <section id="capabilities" className="section skills-section" ref={sectionRef}>
      <div className="section-label">02 — CAPABILITIES</div>
      <h2 className="section-heading">
        Tools I use<br />
        <span className="italic-accent">to turn ideas into products.</span>
      </h2>
      
      <div className="skills-container">
        {portfolioData.skills.map((skillGroup, index) => (
          <div key={index} className="skill-row">
            <div className="skill-category">
              <h3>{skillGroup.category}</h3>
            </div>
            <div className="skill-items">
              {skillGroup.items.map((item, i) => (
                <span key={i} className="skill-item">{item}</span>
              ))}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Skills;
""",

"src/components/Skills.css": """
.skills-section {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 1s ease, transform 1s ease;
  border-top: 1px solid var(--glass-border);
}

.skills-section.visible {
  opacity: 1;
  transform: translateY(0);
}

.skills-container {
  display: flex;
  flex-direction: column;
}

.skill-row {
  display: grid;
  grid-template-columns: 300px 1fr;
  padding: 2.5rem 0;
  border-bottom: 1px solid var(--glass-border);
  align-items: center;
}

.skill-row:first-child {
  border-top: 1px solid var(--glass-border);
}

.skill-category h3 {
  font-family: var(--font-body);
  font-size: 0.85rem;
  letter-spacing: 0.15em;
  color: var(--ink-faint);
}

.skill-items {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.skill-item {
  font-size: 1.1rem;
  color: var(--ink-soft);
  padding: 0.5rem 1.2rem;
  border: 1px solid transparent;
  border-radius: 99px;
  transition: all 0.3s ease;
}

.skill-item:hover {
  color: var(--ink);
  background: var(--glass);
  border-color: var(--glass-border);
  transform: translateY(-2px);
}

@media (max-width: 940px) {
  .skill-row {
    grid-template-columns: 1fr;
    gap: 1.5rem;
    padding: 2rem 0;
  }
}
"""
}

for filepath, content in files.items():
    with open(os.path.join(base_dir, filepath), "w") as f:
        f.write(content)

print("Generated component part 1.")
