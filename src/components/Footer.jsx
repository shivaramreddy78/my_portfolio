import React from 'react';

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
