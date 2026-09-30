import React, { useEffect, useRef } from 'react';
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
