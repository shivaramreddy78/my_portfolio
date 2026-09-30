import React, { useEffect, useRef } from 'react';
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
