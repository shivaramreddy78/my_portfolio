import React, { useEffect, useRef } from 'react';
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
