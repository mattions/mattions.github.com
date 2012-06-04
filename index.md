---
layout: page
title: Hello there!
tagline: Welcome aboard =)
---
{% include JB/setup %}

<div class="row-fluid">
    <div class="span3"><img src="assets/gfx/Michele_Mattioni_sepia.jpg"/> </div>
    
    <div class="span9">
    <p>My name is <strong>Michele Mattioni</strong> and I'm a computational neuroscientist.</p>

    <p>In this pages I'll try to give an overwiew about what I'm up to. To be up to 
    date, you could check out one of the links below, or have a look to the diffrent 
    projects I'm up to.</p>
    
    <ul>
    <li> you can follow me on <a href="http://twitter.com/mattions">twitter</a></li>
    <li> subscribe to my <a href="http://blog.michelemattioni.me/">blog</a></li>
    <li> check out my <a href="http://github.com/mattions/">github</a></li>
    <li> have a look at some of my slides on <a href="http://www.slideshare.net/mattions/">slideshare</a></li>
    <li> visit my profile on <a href="http://www.linkedin.com/pub/michele-mattioni/6/18a/478">linkedin</a></li>
    </ul>
    </div>
</div>



## Projects

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

Thanks for visiting.
