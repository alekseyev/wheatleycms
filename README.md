WheatleyCMS is a CMS solution for [django-nonrel](http://docs.django-nonrel.org). Its codebase is based on [All Buttons Pressed](http://docs.django-nonrel.org/en/latest/content/All%20Buttons%20Pressed%20-%20CMS%20&%20blog%20for%20Django-nonrel.html) project

# Dependencies

- [django-permission-backend-nonrel](https://github.com/django-nonrel/django-permission-backend-nonrel)
- [django-bootstrap](https://github.com/earle/django-bootstrap)
- [django-filetransfers](https://bitbucket.org/wkornewald/django-filetransfers)

Note: WheatleyCMS uses django.contrib.staticfiles for static files management.

# Getting started

First, create an admin user with manage.py createsuperuser. Then, run manage.py runserver and go to [http://localhost:8000/admin/](http://localhost:8000/admin/) and create a few pages and posts. Otherwise you'll only see a 404 error page. A good idea would be to create a blog or page with the url "/".

WheatleyCMS has a concept called "Block". Blocks can be created and edited via the admin UI. The sidebar's content in default template is defined via a block called "sidebar". 

You can also define menus. Use this format:

    Some label     /url
    Other label    http://www.other.url/

You should probably create a menu with the name "menu" (it is used in default template). 

You can use `show_block` and `show_menu` tags in your templates to output blocks and menus. Both of these tags require `{% load cms %}` statement to work.

# Bundled libraries

- [jQuery](http://jquery.com/)
- [Twitter Bootstrap](http://twitter.github.com/bootstrap/)
- [WYSIHTML5](https://github.com/xing/wysihtml5): forked version alekseyev/wysihtml5 
- [Bootstrap-wysihtml5](https://github.com/jhollingworth/bootstrap-wysihtml5)
