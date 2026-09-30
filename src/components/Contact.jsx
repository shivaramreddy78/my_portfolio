import React, { useEffect, useRef } from 'react';
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
        </div>
      </div>
    </section>
  );
};

export default Contact;
