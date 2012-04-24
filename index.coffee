doctype 5
html ->
  head ->
    title 'Title'
    meta name: 'viewport', content: "width:device-width, initial-scale:1.0"
    meta name: 'description', content: ""
    meta name: 'author', content: ""

    link href: 'bootstrap/css/bootstrap.css', rel: 'stylesheet'
    link href: 'bootstrap/css/bootstrap-responsive.css', rel: 'stylesheet'

    link rel: "shortcut icon", href:"bootstrap/ico/favicon.ico"
    link rel: "apple-touch-icon-precomposed", sizes:"114x114", href:"bootstrap/ico/apple-touch-icon-114-precomposed.png"
    link rel: "apple-touch-icon-precomposed", sizes:"72x72", href:"bootstrap/ico/apple-touch-icon-72-precomposed.png"
    link rel: "apple-touch-icon-precomposed", href:"bootstrap/ico/apple-touch-icon-57-precomposed.png"
    
    style -> 
      text 'body {padding-top: 60px}'
      text 'body {padding-bottom: 40px}'


  body ->
      div class:"navbar navbar-fixed-top", ->
          div class:"navbar-inner", ->
            div class:"container", ->
              a class:"btn btn-navbar", 'data-toggle':"collapse", 'data-target': ".nav-collapse", ->
                span class:"icon-bar"
                span class:"icon-bar"
                span class:"icon-bar"
              a class:"brand", href:"#", -> "Michele Mattioni's landapage"
              div class:"nav-collapse", -> 
                ul class:"nav", -> 
                  li class:"active", -> 
                    a href:"#", -> 'Home'
                  li -> 
                    a href:"#about", -> 'About'
                  li -> 
                    a href:"#contact", -> 'Contact'
    
    div class:"container", ->
        div class:"hero-unit", ->
            h1 -> "Hello there!"
            p -> "This is my landing page, where you can find the link to all the 
                    stuff I tend to do on internet"
            
        
        div class:"row", ->
            div class:"span4", id:"twitter_feed", -> 
                h2 -> "Twitter feed"
                p -> "Here goes the twitter feed "
            
            div class:"span4", id:"google_plus", ->
                h2 -> "Google feed"
                p -> "Google plus feed"
                
            div class:"span4", id:"blog_feed", ->
                h2 -> "Blog Feed"
                p -> "blog feed"
                
                
    
    script src: "lib/jquery-1.7.2.js"
    script src: 'lib/bootstrap-2.0.2/js/bootstrap.js'
    
        
    
        
        
