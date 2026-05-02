# Michele Mattioni's Website

A modern, responsive personal website showcasing research and blog posts on computational neuroscience, data science, and technology.

## Tech Stack

This is a **pure static HTML** site — no build step, no dependencies. Just clean HTML5 + CSS3.

### Design

- **Fonts**: Playfair Display (headings) + Inter (body) via Google Fonts
- **Colors**: Navy (#0f1c2e), Teal (#2e7d88), Slate (#5a6577)
- **Features**: Sticky frosted-glass navbar, responsive layout, fade-in animations, mobile hamburger menu

### Structure

```
.
├── index.html          # Homepage with hero + latest posts
├── archive.html        # All posts by date
├── tags.html           # Posts grouped by tags
├── categories.html     # Posts grouped by category
├── pages.html          # Site pages
├── posts/              # Individual blog post pages
├── 404.html            # Custom 404 page
└── assets/
    └── themes/twitter-2.0-cyborg/
        └── css/
            └── style.css    # All styling
```

## Development

No build tools needed. Just open `index.html` in a browser or serve with:

```bash
python3 -m http.server 8000
```

## Content

The site contains 6 blog posts spanning topics in:
- Computational neuroscience (NeuroML, neuron modeling)
- Scientific computing
- Sustainable technology
- Bitcoin payments
