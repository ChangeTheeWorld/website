# website
the website for the Change The World Initiative.

# run
```commandline
python manage.py runserver localhost:8000
```
after that, to get access to tailwind, also run
```commandline
python manage.py tailwind start
```

# apps
## blog
the urls with a prefix `/blog/`, used for the blog (duh)

## home
the homepage of the site.

## theme
idk what it is, but it's required for working with tailwind in Django.
please don't touch anything in that app unless you want to change the tailwind config,
in which case the path is `theme/static_src/tailwind.config.js`.