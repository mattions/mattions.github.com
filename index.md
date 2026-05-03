---
layout: default
title: Home
description: Computational Neuroscience, Open Source Software, and Sustainable Technology — by Michele Mattioni
---
<div class="container">
  <section class="index-hero">
    <h1>Hi, I'm Michele. <em>Researcher & Developer.</em></h1>
    <p>I work at the intersection of <strong>computational neuroscience</strong>, <strong>open source software</strong>, and <strong>sustainable technology</strong>. Here are some of the projects I've built over the years.</p>
    <div class="hero-divider"></div>
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
