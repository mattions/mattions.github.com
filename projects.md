---
layout: default
title: Projects
---
<div class="container">
  <section class="section-header">
    <h1>Projects</h1>
  </section>

  <div class="projects-grid">
    {% for post in site.posts %}
    <a href="{{ post.url | relative_url }}" class="project-card">
      <div class="project-card-header">
        <span class="project-date">{{ post.date | date: "%b %Y" }}</span>
      </div>
      <h2>{{ post.title }}</h2>
      <p>{{ post.description | strip_html }}</p>
      <div class="project-tags">
        {% for tag in post.tags %}
        <span class="tag">{{ tag }}</span>
        {% endfor %}
      </div>
      <div class="project-arrow"></div>
    </a>
    {% endfor %}
  </div>
</div>
