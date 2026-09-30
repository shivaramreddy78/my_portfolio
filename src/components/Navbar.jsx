import React, { useState, useEffect } from 'react';
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

          <a href="#contact">Contact</a>
        </div>

        <div className="nav-cta desktop-only">
          <a href="#contact" onClick={(e) => { e.preventDefault(); document.getElementById('contact')?.scrollIntoView({behavior: 'smooth'}); }} className="pill-button">
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

          <a href="#contact" onClick={() => setMenuOpen(false)}>Contact</a>
          <a href="#contact" className="pill-button" onClick={(e) => { e.preventDefault(); setMenuOpen(false); document.getElementById('contact')?.scrollIntoView({behavior: 'smooth'}); }}>
            Let's Talk <ArrowUpRight />
          </a>
        </div>
      )}
    </header>
  );
};

export default Navbar;
