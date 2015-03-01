## Website

My personal website set up using [Jekyll boostrap] (http://jekyllbootstrap.com/) and [jekyll] 
(https://github.com/mojombo/jekyll).

To develop locally just run:

```jekyll server```

select proper ruby interpreter with 

```rvm use defaul```

## Update the theme

For some reason the Rake theme:install does not work properly and does not override.
A quick hack to get this working is to remove the two directory belonging to the theme:

```
rm -rv _includes/themes/twitter-2.0-cyborg/ assets/themes/twitter-2.0-cyborg/
```

and then procede with the classic 

```
rake theme:install git="https://github.com/mattions/theme-twitter-2.0-cyborg"
```
