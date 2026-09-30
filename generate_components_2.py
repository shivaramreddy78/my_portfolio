import os

base_dir = "/Users/shivaramreddy/projects/protfolio"

files = {
"src/components/Projects.jsx": """import React, { useEffect, useRef } from 'react';
import { portfolioData } from '../data/portfolio';
import { ArrowUpRight } from './icons';

const Projects = () => {
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
    <section id="projects" className="section projects-section" ref={sectionRef}>
      <div className="section-label">03 — SELECTED WORK</div>
      <h2 className="section-heading">
        Projects built<br />
        <span className="italic-accent">to solve real problems.</span>
      </h2>

      <div className="projects-grid">
        {portfolioData.projects.map((project, index) => (
          <div key={index} className={`project-card ${index % 2 !== 0 ? 'offset' : ''}`}>
            <a href={project.link} className="project-link-wrapper">
              <div className="project-visual">
                <div className="project-number">{project.id}</div>
                <div className="project-overlay"></div>
              </div>
              <div className="project-content">
                <h3 className="project-title">{project.title}</h3>
                <p className="project-desc">{project.description}</p>
                <div className="project-meta">
                  <div className="project-tech">
                    {project.tech.map((t, i) => (
                      <span key={i}>{t}</span>
                    ))}
                  </div>
                  <div className="project-cta">
                    View Project <ArrowUpRight />
                  </div>
                </div>
              </div>
            </a>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Projects;
""",

"src/components/Projects.css": """
.projects-section {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 1s ease, transform 1s ease;
}

.projects-section.visible {
  opacity: 1;
  transform: translateY(0);
}

.projects-grid {
  display: flex;
  flex-direction: column;
  gap: 6rem;
  margin-top: 4rem;
}

.project-card {
  width: 100%;
  max-width: 1000px;
}

.project-card.offset {
  align-self: flex-end;
}

.project-link-wrapper {
  display: block;
  text-decoration: none;
  color: inherit;
  group: hover;
}

.project-visual {
  position: relative;
  width: 100%;
  aspect-ratio: 16/9;
  background: var(--ground-deep);
  border: 1px solid var(--glass-border);
  border-radius: 24px;
  overflow: hidden;
  margin-bottom: 2rem;
  transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  align-items: center;
  justify-content: center;
}

.project-visual::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at center, rgba(255,255,255,0.05) 0%, transparent 60%);
  opacity: 0.5;
  transition: opacity 0.5s ease;
}

.project-number {
  font-family: var(--font-display);
  font-size: 10rem;
  font-weight: 700;
  color: var(--ink-ghost);
  opacity: 0.2;
  transition: transform 0.5s ease, opacity 0.5s ease;
}

.project-content {
  padding: 0 1rem;
}

.project-title {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: var(--ink);
  transition: color 0.3s ease;
}

.project-desc {
  font-size: 1.1rem;
  color: var(--ink-soft);
  margin-bottom: 1.5rem;
  max-width: 700px;
}

.project-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid var(--glass-border);
  padding-top: 1.5rem;
  transition: border-color 0.3s ease;
}

.project-tech {
  display: flex;
  flex-wrap: wrap;
  gap: 0.8rem;
}

.project-tech span {
  font-size: 0.8rem;
  letter-spacing: 0.05em;
  color: var(--ink-faint);
  text-transform: uppercase;
}

.project-cta {
  display: flex;
  align-items: center;
  font-size: 0.9rem;
  color: var(--ink-soft);
  transition: color 0.3s ease;
}

/* Hover Effects */
.project-link-wrapper:hover .project-visual {
  transform: translateY(-8px);
  border-color: var(--ink-faint);
  box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}

.project-link-wrapper:hover .project-visual::before {
  opacity: 1;
}

.project-link-wrapper:hover .project-number {
  transform: scale(1.05);
  opacity: 0.4;
  color: var(--flame);
}

.project-link-wrapper:hover .project-title {
  color: var(--ink);
}

.project-link-wrapper:hover .project-meta {
  border-color: var(--ink-faint);
}

.project-link-wrapper:hover .project-cta {
  color: var(--flame);
}

.project-link-wrapper:hover .project-cta svg {
  transform: translate(3px, -3px);
}

@media (max-width: 940px) {
  .project-card.offset {
    align-self: flex-start;
  }
  .projects-grid {
    gap: 4rem;
  }
  .project-visual {
    aspect-ratio: 4/3;
  }
  .project-number {
    font-size: 6rem;
  }
  .project-meta {
    flex-direction: column;
    align-items: flex-start;
    gap: 1.5rem;
  }
}
""",

"src/components/Experience.jsx": """import React, { useEffect, useRef } from 'react';
import { portfolioData } from '../data/portfolio';

const Experience = () => {
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
    <section id="experience" className="section experience-section" ref={sectionRef}>
      <div className="section-label">04 — EXPERIENCE</div>
      <h2 className="section-heading">
        Learning by<br />
        <span className="italic-accent">building.</span>
      </h2>

      <div className="experience-timeline">
        {portfolioData.experience.map((exp, index) => (
          <div key={index} className="timeline-item">
            <div className="timeline-dot"></div>
            <div className="timeline-content">
              <div className="timeline-meta">
                <h3 className="company">{exp.company}</h3>
                <span className="date">{exp.date}</span>
              </div>
              <h4 className="role">{exp.role}</h4>
              {exp.description && <p className="desc">{exp.description}</p>}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Experience;
""",

"src/components/Experience.css": """
.experience-section {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 1s ease, transform 1s ease;
  border-top: 1px solid var(--glass-border);
}

.experience-section.visible {
  opacity: 1;
  transform: translateY(0);
}

.experience-timeline {
  margin-top: 4rem;
  position: relative;
  max-width: 800px;
}

.experience-timeline::before {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  left: 5px;
  width: 1px;
  background: var(--glass-border);
}

.timeline-item {
  position: relative;
  padding-left: 3rem;
  margin-bottom: 4rem;
}

.timeline-item:last-child {
  margin-bottom: 0;
}

.timeline-dot {
  position: absolute;
  top: 6px;
  left: 0;
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: var(--ground-deep);
  border: 1px solid var(--flame);
  box-shadow: 0 0 10px rgba(255, 74, 0, 0.2);
}

.timeline-content {
  background: var(--glass);
  border: 1px solid var(--glass-border);
  padding: 2rem;
  border-radius: 16px;
  transition: transform 0.3s ease, border-color 0.3s ease;
}

.timeline-content:hover {
  transform: translateX(10px);
  border-color: var(--ink-faint);
}

.timeline-meta {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 0.5rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.company {
  font-family: var(--font-display);
  font-size: 1.2rem;
  color: var(--ink);
  letter-spacing: 0.05em;
}

.date {
  font-size: 0.85rem;
  color: var(--ink-faint);
  font-family: var(--font-body);
}

.role {
  font-size: 1rem;
  color: var(--flame-lit);
  margin-bottom: 1rem;
  font-weight: 400;
}

.desc {
  color: var(--ink-soft);
  line-height: 1.6;
  font-size: 0.95rem;
}

@media (max-width: 768px) {
  .timeline-meta {
    flex-direction: column;
    gap: 0.2rem;
  }
}
""",

"src/components/Achievements.jsx": """import React, { useEffect, useRef } from 'react';
import { portfolioData } from '../data/portfolio';

const Achievements = () => {
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
    <section className="section achievements-section" ref={sectionRef}>
      <div className="section-label">05 — ACHIEVEMENTS</div>
      
      <div className="achievements-grid">
        {portfolioData.achievements.map((item, index) => (
          <div key={index} className="achievement-card">
            <div className="achievement-number">{item.number}</div>
            <div className="achievement-content">
              <h3>{item.title}</h3>
              {item.subtitle && <p>{item.subtitle}</p>}
            </div>
          </div>
        ))}
      </div>

      <div className="education-block">
        <div className="section-label">06 — EDUCATION</div>
        <h3>B.Tech — Computer Science & Engineering</h3>
      </div>
    </section>
  );
};

export default Achievements;
""",

"src/components/Achievements.css": """
.achievements-section {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 1s ease, transform 1s ease;
}

.achievements-section.visible {
  opacity: 1;
  transform: translateY(0);
}

.achievements-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 6rem;
}

.achievement-card {
  position: relative;
  padding: 3rem 2rem;
  background: var(--glass);
  border: 1px solid var(--glass-border);
  border-radius: 20px;
  overflow: hidden;
  transition: transform 0.3s ease, background 0.3s ease;
}

.achievement-card:hover {
  transform: translateY(-5px);
  background: var(--glass-hover);
  border-color: var(--ink-faint);
}

.achievement-number {
  position: absolute;
  top: -10px;
  right: -10px;
  font-family: var(--font-display);
  font-size: 6rem;
  font-weight: 700;
  color: var(--ink-ghost);
  opacity: 0.3;
  line-height: 1;
}

.achievement-content {
  position: relative;
  z-index: 1;
  margin-top: 2rem;
}

.achievement-content h3 {
  font-size: 1.2rem;
  color: var(--ink);
  margin-bottom: 0.5rem;
}

.achievement-content p {
  font-size: 0.9rem;
  color: var(--ink-soft);
}

.education-block {
  padding: 4rem 0;
  border-top: 1px solid var(--glass-border);
  text-align: center;
}

.education-block h3 {
  font-size: clamp(1.5rem, 3vw, 2.5rem);
  color: var(--ink);
  font-weight: 400;
}
""",

"src/components/Contact.jsx": """import React, { useEffect, useRef } from 'react';
import { portfolioData } from '../data/portfolio';
import { ArrowUpRight } from './icons';

const Contact = () => {
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
    <section id="contact" className="contact-section" ref={sectionRef}>
      <div className="contact-container">
        <div className="section-label">07 — CONTACT</div>
        
        <h2 className="contact-heading">
          Have an idea?<br />
          <span className="italic-accent">Let's build it.</span>
        </h2>
        
        <p className="contact-desc">
          I'm open to interesting projects, collaborations,<br />
          internships and opportunities to build useful technology.
        </p>

        <div className="contact-links">
          <a href={`mailto:${portfolioData.contact.email}`} className="pill-button primary">
            Email Me <ArrowUpRight />
          </a>
          <a href={portfolioData.contact.github} target="_blank" rel="noopener noreferrer" className="pill-button">
            GitHub <ArrowUpRight />
          </a>
          <a href={portfolioData.contact.linkedin} target="_blank" rel="noopener noreferrer" className="pill-button">
            LinkedIn <ArrowUpRight />
          </a>
        </div>
      </div>
    </section>
  );
};

export default Contact;
""",

"src/components/Contact.css": """
.contact-section {
  padding: 10rem 5%;
  background: var(--ground-deep);
  border-top: 1px solid var(--glass-border);
  position: relative;
  overflow: hidden;
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 1s ease, transform 1s ease;
}

.contact-section.visible {
  opacity: 1;
  transform: translateY(0);
}

.contact-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100vw;
  height: 500px;
  background: radial-gradient(circle at top, rgba(255, 74, 0, 0.05) 0%, transparent 70%);
  pointer-events: none;
}

.contact-container {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
  position: relative;
  z-index: 2;
}

.contact-container .section-label {
  display: inline-block;
}

.contact-heading {
  font-size: clamp(3rem, 6vw, 5rem);
  margin-bottom: 2rem;
  color: var(--ink);
}

.contact-desc {
  font-size: 1.1rem;
  color: var(--ink-soft);
  margin-bottom: 4rem;
  line-height: 1.6;
}

.contact-links {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 1rem;
}

@media (max-width: 768px) {
  .contact-links {
    flex-direction: column;
    align-items: stretch;
  }
}
""",

"src/components/Footer.jsx": """import React from 'react';

const Footer = () => {
  return (
    <footer className="footer-section">
      <div className="footer-content">
        <div className="footer-left">
          SHIVARAM REDDY
        </div>
        <div className="footer-center">
          FULL STACK · AI · WEB
        </div>
        <div className="footer-right">
          © {new Date().getFullYear()}
        </div>
      </div>
      <div className="footer-watermark">
        BUILD
      </div>
    </footer>
  );
};

export default Footer;
""",

"src/components/Footer.css": """
.footer-section {
  position: relative;
  padding: 2rem 5% 4rem;
  background: var(--ground-deep);
  border-top: 1px solid var(--glass-border);
  overflow: hidden;
}

.footer-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.8rem;
  color: var(--ink-faint);
  letter-spacing: 0.05em;
  position: relative;
  z-index: 2;
  max-width: 1400px;
  margin: 0 auto;
}

.footer-watermark {
  position: absolute;
  bottom: -4vw;
  left: 50%;
  transform: translateX(-50%);
  font-family: var(--font-display);
  font-size: 25vw;
  font-weight: 700;
  line-height: 1;
  color: var(--ink-ghost);
  opacity: 0.02;
  pointer-events: none;
  z-index: 1;
  white-space: nowrap;
}

@media (max-width: 768px) {
  .footer-content {
    flex-direction: column;
    gap: 1.5rem;
    text-align: center;
  }
  .footer-watermark {
    font-size: 35vw;
    bottom: 2vw;
  }
}
"""
}

for filepath, content in files.items():
    with open(os.path.join(base_dir, filepath), "w") as f:
        f.write(content)

print("Generated component part 2.")
