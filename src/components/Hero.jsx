import React from 'react';
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


    </section>
  );
};

export default Hero;
