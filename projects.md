---
layout: default
title: Projects
---
<div class="container">
  <section class="index-hero">
    <h1>Projects</h1>
    <p>A collection of work spanning computational neuroscience, open source software, and sustainable technology.</p>
  </section>

  <ul class="projects-list">
    {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}" class="project-item">
        <span class="project-date">{{ post.date | date: "%b %Y" }}</span>
        <div class="project-meta">
          <h2>{{ post.title }}</h2>
          <p>{{ post.description | strip_html | truncatewords: 24 }}</p>
          <div class="project-tags">
            {% for tag in post.tags %}
            <span class="tag">{{ tag }}</span>
            {% endfor %}
          </div>
        </div>
      </a>
    </li>
    {% endfor %}
  </ul>
</div>
