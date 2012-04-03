doctype 5
html ->
  head ->
    meta charset: 'utf-8'
    title "Michele Mattioni\'s webpage"
    script src: "lib/jquery-1.7.2.js"
    script src: 'lib/bootstrap-2.0.2/js/bootstrap.js'
    #script src: 'src/search-client.js'
    link rel: 'stylesheet', href: 'lib/bootstrap-2.0.2/css/slate-bootstrap.min.css'
    #link rel: 'stylesheet', href: 'lib/bootstrap-2.0.2/css/cerulan-bootstrap.min.css'
    #link rel: 'stylesheet', href: 'lib/bootstrap-2.0.2/css/bootstrap.min.css'

  body '.container', ->
    h1 -> "Mattioni Michele\'s webpage"
    
    div class: 'span-12', ->
        h2 -> "What\'s going on"
        div class: 'span-4', id: 'twitter_feed', -> 
            p -> "Here goes the twitter feed "
        
        div class: 'span-4', id: 'google_plus', ->
            p -> "Google plus feed"
            
        div class: 'span-4', id: 'blog_feed', ->
            p -> "blog feed"
    
        
    
        
        
