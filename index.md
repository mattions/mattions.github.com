---
layout: page
title: Hello there!
tagline: Welcome aboard =)
---
{% include JB/setup %}

<div class="row-fluid">
    <div class="span2"><img src="assets/gfx/Michele_Mattioni_sepia.jpg"/> </div>
    
    <div class="span6">
    <p>My name is <strong>Michele Mattioni</strong> and I'm a computational neuroscientist. 
    I've obtained my Bachelor (hons) from the <a href="http://www.univpm.it/">Università 
    Politecnica delle Marche</a>, then my Master Of Science (hons) from the 
    <a href="http://www.unicam.it/">Università di Camerino</a>, and then I've done 
    my joint PhD at the <a href="http://www.cam.ac.uk/">University of Cambridge</a> 
    and the <a href="http://www.ebi.ac.uk">EMBL-EBI</a>.</p>

    <p>To be up to date with my latest endevours, you could check out one of the 
    links below, or have a look to the different projects I'm up to in the projects 
    section. Over there I've summarized some of the projects I have undergoing 
    or I've done in the past.</p>
    
    <p> You can email me at <a href="mailto:mattions@gmail.com">mattions@gmail.com</a>, or</p>
    
    <ul>
    <li> you can follow me on <a href="http://twitter.com/mattions">twitter</a></li>
    <li> subscribe to my <a href="http://blog.michelemattioni.me/">blog</a></li>
    <li> check out my <a href="http://github.com/mattions/">github</a></li>
    <li> have a look at some of my slides on <a href="http://www.slideshare.net/mattions/">slideshare</a></li>
    <li> visit my profile on <a href="http://www.linkedin.com/pub/michele-mattioni/6/18a/478">linkedin</a></li>
    
    </ul>
    </div>
    <div class="span3">
    <script charset="utf-8" src="http://widgets.twimg.com/j/2/widget.js"></script>
<script>
new TWTR.Widget({
  version: 2,
  type: 'search',
  search: 'from:mattions',
  interval: 30000,
  title: 'Tweets from Michele',
  subject: '',
  width: 250,
  height: 300,
  theme: {
    shell: {
      background: '#8ec1da',
      color: '#ffffff'
    },
    tweets: {
      background: '#ffffff',
      color: '#444444',
      links: '#1985b5'
    }
  },
  features: {
    scrollbar: false,
    loop: true,
    live: true,
    behavior: 'default'
  }
}).render().start();
</script>
    
    
    
    </div>
</div>



## Projects

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

Thanks for visiting.
