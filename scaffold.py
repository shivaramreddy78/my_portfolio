import os

base_dir = "/Users/shivaramreddy/projects/protfolio"

dirs = [
    "src/components",
    "src/data",
    "src/styles",
]

for d in dirs:
    os.makedirs(os.path.join(base_dir, d), exist_ok=True)

files = {
    "src/components/Navbar.jsx": "",
    "src/components/Navbar.css": "",
    "src/components/Hero.jsx": "",
    "src/components/Hero.css": "",
    "src/components/About.jsx": "",
    "src/components/About.css": "",
    "src/components/Skills.jsx": "",
    "src/components/Skills.css": "",
    "src/components/Projects.jsx": "",
    "src/components/Projects.css": "",
    "src/components/Experience.jsx": "",
    "src/components/Experience.css": "",
    "src/components/Achievements.jsx": "",
    "src/components/Achievements.css": "",
    "src/components/Contact.jsx": "",
    "src/components/Contact.css": "",
    "src/components/Footer.jsx": "",
    "src/components/Footer.css": "",
    "src/components/icons.jsx": "",
    "src/data/portfolio.js": "",
    "src/styles/globals.css": "",
}

for filepath, content in files.items():
    with open(os.path.join(base_dir, filepath), "w") as f:
        f.write(content)

print("Scaffolded structure.")
