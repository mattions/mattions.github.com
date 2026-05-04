# Michele Mattioni — Portfolio & Blog

Personal portfolio site and blog built with Jekyll, hosted on GitHub Pages.

> **Live site:** [michelemattioni.me](https://michelemattioni.me)  
> **GitHub Pages:** [mattions.github.io](https://mattions.github.io)

---

## ⚡ Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/mattions/mattions.github.com.git
cd mattions.github.com

# 2. (Optional) Install Jekyll
gem install jekyll bundler

# 3. Serve locally
jekyll serve

# 4. Open http://localhost:4000
```

No Ruby installed? Use Python as a fallback:

```bash
python3 -m http.server 8080
# Open http://localhost:8080
```

---

## 📦 Dependencies

| Dependency | Purpose | Required? |
|---|---|---|
| **Jekyll** (v3.9+) | Static site generator — provided by GitHub Pages automatically | Optional for local dev |
| **Bundler** | Ruby gem management | Optional for local dev |
| **Python 3** (3.6+) | Fallback static server (`http.server`) | Optional |

No npm, no build tools, no compiled dependencies.

### Installing Jekyll (macOS / Linux)

```bash
# 1. Install Ruby (if not already installed)
# macOS:
ruby -v  # if missing: brew install ruby

# Linux (Debian/Ubuntu):
sudo apt install ruby ruby-dev build-essential

# 2. Install Jekyll + Bundler
gem install jekyll bundler

# 3. Build and serve
bundle exec jekyll serve --livereload
```

### Installing Jekyll (Windows)

```powershell
# Use RubyInstaller: https://rubyinstaller.org
# Then:
gem install jekyll bundler
jekyll serve
```

---

## 🛠 Development

### Project Structure

```
.
├── _config.yml              # Site config (title, author, URLs)
├── _layouts/                # HTML templates
│   ├── default.html         # Base layout (nav + footer)
│   ├── post.html            # Blog post template
│   └── page.html            # Static page template
├── _posts/                  # Blog posts
│   ├── 2012-06-01-neuronvisio.md
│   ├── 2012-06-04-multiscale-modelling.md
│   └── ...
├── assets/
│   ├── css/main.css         # All custom styles
│   └── gfx/                 # Images & graphics
├── index.html               # Homepage
├── 404.html                 # Custom 404 page
├── archive.html             # Post archive
├── categories.html          # Categories listing
├── tags.html                # Tags listing
├── AGENTS.md                # Repo structure & dev guide
├── screenshot-*.png         # PR screenshots
└── .gitignore
```

### Adding a Blog Post

Create a file in `_posts/` named `YYYY-MM-DD-your-post-title.md`:

```yaml
---
layout: post
title: "Your Post Title"
date: 2026-01-01 12:00:00 +0000
category: category-name
tags: [tag1, tag2]
description: "A short description"
---

Post content here. Markdown is supported.
```

The filename date and the YAML `date` should match.

### Adding a Static Page

Create a file in the repo root:

```yaml
---
layout: page
title: Page Title
---

Content here.
```

### Customizing the Design

All styles are in `assets/css/main.css`. Key CSS variables are defined in `:root`:

```css
:root {
  --bg-primary: #f8f9fc;       /* Page background */
  --text-primary: #1a1a2e;     /* Main text color */
  --accent-blue: #4a9eff;      /* Primary accent */
  --accent-purple: #8b5cf6;    /* Secondary accent */
  --gradient-text: linear-gradient(135deg, #4a9eff, #8b5cf6, #ec4899);
  /* ... more variables */
}
```

### Previewing Locally

```bash
# With Jekyll (full build, includes posts)
jekyll serve --livereload

# Without Jekyll (static files only, no post rendering)
python3 -m http.server 8080
```

---

## 📸 Screenshots

PR screenshots are committed to the repo:

| File | Shows |
|------|-------|
| `screenshot-hero.png` | Hero section (photo, bio, social links) |
| `screenshot-projects.png` | Projects grid with glassmorphism cards |
| `screenshot-blog.png` | Live blog RSS feed |
| `screenshot-full.png` | Full page scroll |
| `screenshot-bottom.png` | Footer area |

---

## 🚀 Deployment

This repo uses **GitHub Pages** with automatic Jekyll builds from the `master` branch.

1. Push to `master` → GitHub Pages builds and deploys automatically
2. Custom domain configured via `CNAME` → `michelemattioni.me`
3. No CI/CD pipeline needed

**Note:** GitHub Pages uses Jekyll v3.9+ which supports most modern Liquid filters. Check [GitHub Pages docs](https://pages.github.com/) for the exact version.

---

## 📝 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feat/your-feature`)
3. Make your changes
4. Commit with [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`, etc.)
5. Push and open a Pull Request

---

## 📄 License

All content and code © Michele Mattioni
