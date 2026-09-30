import React, { useEffect, useRef } from 'react';
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
