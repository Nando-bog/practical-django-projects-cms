CMS Project from the book Practical Django Projects, updated to Django 1.6.

Bennett, J. (2008). Practical Django Projects (Expert’s Voice in Web Development) (1 edition.). Apress.


A few things did not work, as was expected. But it ended well, and it was an interesting learning experience.

Most difficult issue was the editor. TinyMCE integration as described did not work. I ended up using CKEditor with django-ckeditor-updated (https://github.com/riklaunim/django-ckeditor) and some borrowed code from https://gist.github.com/elidickinson/1379652 to add the editor to the Flatpages admin.

The project is functional with an extra "home page" at /, home, index and index.html that shows a list of all static pages in the cms. Good learning experience.

This is a full working version of the project for Django 1.6 and the following requirements:
Django==1.6.1
django-ckeditor-updated==4.2.6
psycopg2==2.5.1
wsgiref==0.1.2

-----The file browser in CKEditor still does not work. I do not plan to work on fixing it for this project.------