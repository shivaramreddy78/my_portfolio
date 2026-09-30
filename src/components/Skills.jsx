import React, { useEffect, useRef } from 'react';
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
