import os

base_dir = "/Users/shivaramreddy/projects/protfolio"

files = {
"index.html": """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Shivaram Reddy — Full Stack Developer & AI Developer</title>
    <meta name="description" content="Portfolio of Shivaram Reddy — Full Stack Developer building modern web applications, AI-powered products and digital experiences." />
    <meta name="theme-color" content="#160703" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@1&family=Inter+Tight:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
""",

"src/data/portfolio.js": """export const portfolioData = {
  about: {
    description1: "I'm Shivaram Reddy, a B.Tech Computer Science student and developer focused on building full-stack web applications, AI-powered systems, and practical digital products.",
    description2: "I enjoy taking an idea from concept to a working product — designing the interface, building the backend, connecting APIs, integrating AI, and turning everything into a usable experience."
  },
  skills: [
    {
      category: "FRONTEND",
      items: ["React", "JavaScript", "HTML", "CSS", "Responsive Design"]
    },
    {
      category: "BACKEND",
      items: ["Python", "FastAPI", "Node.js", "REST APIs"]
    },
    {
      category: "DATABASE",
      items: ["SQLite", "SQL", "Supabase"]
    },
    {
      category: "AI / ML",
      items: ["Generative AI", "Computer Vision", "MediaPipe", "OpenAI APIs", "Groq", "LLM Integration"]
    },
    {
      category: "TOOLS",
      items: ["Git", "GitHub", "VS Code", "Antigravity", "Streamlit"]
    },
    {
      category: "CLOUD / DEVELOPMENT",
      items: ["AWS", "API Integration", "Deployment", "Version Control"]
    }
  ],
  projects: [
    {
      id: "01",
      title: "SMART POSTURE",
      description: "A privacy-first computer vision application that analyzes posture through a webcam and provides real-time feedback without storing camera frames or personal data.",
      tech: ["Python", "OpenCV", "MediaPipe", "Computer Vision"],
      link: "#"
    },
    {
      id: "02",
      title: "PATTERN OPTIMA",
      description: "An AI-assisted solution designed to reduce fabric waste in garment production through intelligent 2D pattern nesting and visualization.",
      tech: ["React", "AI", "2D Nesting", "SQLite", "Supabase"],
      link: "#"
    },
    {
      id: "03",
      title: "SMART SUMMARIZER",
      description: "An AI-powered multimedia summarization application that combines speech recognition and language models to turn long-form content into concise summaries. (12+ Languages, Research Publication)",
      tech: ["Groq Whisper", "Llama", "LangChain", "Streamlit", "FFmpeg", "yt-dlp"],
      link: "#"
    },
    {
      id: "04",
      title: "AI ALTERNATIVE CREDIT ASSESSMENT",
      description: "An AI-based alternative credit assessment concept using business, cashflow and financial signals to support more informed assessment of underserved small businesses.",
      tech: ["FastAPI", "Python", "SQLAlchemy", "SQLite", "Supabase", "AI"],
      link: "#"
    }
  ],
  experience: [
    {
      company: "SANGAM SOLUTIONS",
      role: "Generative AI Intern",
      date: "June – July 2024",
      description: "Worked with Salesforce chatbot concepts and Workato automation workflows."
    },
    {
      company: "PANTECH SOLUTIONS",
      role: "Full Stack Development Intern",
      date: "April – July 2024",
      description: "Worked with Git/GitHub, API integration, web development and deployment workflows."
    },
    {
      company: "TLI HYDERABAD",
      role: "IoT Intern",
      date: "July 2023",
      description: ""
    }
  ],
  achievements: [
    {
      number: "02",
      title: "2nd Prize",
      subtitle: "Generative AI Hackathon"
    },
    {
      number: "01",
      title: "1st Prize",
      subtitle: "Paper Presentation"
    },
    {
      number: "01",
      title: "Best Active Programmer",
      subtitle: ""
    },
    {
      number: "CSE",
      title: "Department Overall Head",
      subtitle: ""
    }
  ],
  contact: {
    email: "YOUR_EMAIL@example.com",
    github: "YOUR_GITHUB_URL",
    linkedin: "YOUR_LINKEDIN_URL"
  }
};
""",

"src/styles/globals.css": """
:root {
  --ground: #160703;
  --ground-deep: #090302;
  --ink: #ffffff;
  --ink-soft: rgba(255,255,255,.72);
  --ink-faint: rgba(255,255,255,.46);
  --ink-ghost: rgba(255,255,255,.16);

  --flame: #ff4a00;
  --flame-lit: #ff9a3d;

  --glass: rgba(255,255,255,.06);
  --glass-border: rgba(255,255,255,.12);
  --glass-hover: rgba(255,255,255,.09);

  --font-display: 'Inter Tight', sans-serif;
  --font-body: 'Inter', sans-serif;
  --font-accent: 'Instrument Serif', serif;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
  background-color: var(--ground-deep);
  color: var(--ink);
}

body {
  font-family: var(--font-body);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  line-height: 1.5;
  overflow-x: hidden;
  background: var(--ground);
  background-image: 
    radial-gradient(circle at 15% 50%, rgba(255, 74, 0, 0.05) 0%, transparent 50%),
    radial-gradient(circle at 85% 30%, rgba(255, 154, 61, 0.03) 0%, transparent 50%);
}

h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-display);
  font-weight: 500;
  line-height: 1.1;
  letter-spacing: -0.02em;
}

a {
  color: inherit;
  text-decoration: none;
}

ul {
  list-style: none;
}

img {
  max-width: 100%;
  display: block;
}

.pill-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.8rem 1.6rem;
  border-radius: 99px;
  font-family: var(--font-body);
  font-weight: 500;
  font-size: 0.9rem;
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  cursor: pointer;
  border: 1px solid var(--glass-border);
  background: var(--glass);
  color: var(--ink);
  backdrop-filter: blur(12px);
}

.pill-button:hover {
  background: var(--glass-hover);
  border-color: var(--ink-faint);
  transform: translateY(-2px);
}

.pill-button.primary {
  background: var(--ink);
  color: var(--ground-deep);
  border: none;
}

.pill-button.primary:hover {
  background: var(--ink-soft);
  transform: translateY(-2px);
}

.section {
  padding: 8rem 5%;
  position: relative;
  z-index: 2;
}

.section-label {
  font-family: var(--font-display);
  font-size: 0.8rem;
  letter-spacing: 0.1em;
  color: var(--ink-faint);
  margin-bottom: 2rem;
  text-transform: uppercase;
}

.section-heading {
  font-size: clamp(2.5rem, 5vw, 4rem);
  max-width: 800px;
  margin-bottom: 4rem;
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
""",

"src/components/icons.jsx": """export const ArrowUpRight = () => (
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{marginLeft: '0.4rem', transition: 'transform 0.3s'}}>
    <line x1="7" y1="17" x2="17" y2="7"></line>
    <polyline points="7 7 17 7 17 17"></polyline>
  </svg>
);

export const ArrowRight = () => (
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{marginLeft: '0.4rem', transition: 'transform 0.3s'}}>
    <line x1="5" y1="12" x2="19" y2="12"></line>
    <polyline points="12 5 19 12 12 19"></polyline>
  </svg>
);

export const ArrowDown = () => (
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <line x1="12" y1="5" x2="12" y2="19"></line>
    <polyline points="19 12 12 19 5 12"></polyline>
  </svg>
);
""",

"src/App.jsx": """import React from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import About from './components/About';
import Skills from './components/Skills';
import Projects from './components/Projects';
import Experience from './components/Experience';
import Achievements from './components/Achievements';
import Contact from './components/Contact';
import Footer from './components/Footer';

function App() {
  return (
    <>
      <Navbar />
      <main>
        <Hero />
        <About />
        <Skills />
        <Projects />
        <Experience />
        <Achievements />
        <Contact />
      </main>
      <Footer />
    </>
  );
}

export default App;
""",

"src/main.jsx": """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './styles/globals.css'
import './components/Navbar.css'
import './components/Hero.css'
import './components/About.css'
import './components/Skills.css'
import './components/Projects.css'
import './components/Experience.css'
import './components/Achievements.css'
import './components/Contact.css'
import './components/Footer.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
"""
}

for filepath, content in files.items():
    with open(os.path.join(base_dir, filepath), "w") as f:
        f.write(content)

print("Generated core files.")
