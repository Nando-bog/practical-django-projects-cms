Project from: Bennett, J. (2008). Practical Django Projects (Expert’s Voice in Web Development) (1 edition.). Apress.

Attempting it with the following requirments:
Python==2.7.5
Django==1.6.1
psycopg2==2.5.1
wsgiref==0.1.2

In the CMS project, the TinyMCE integration did not work. Ended up using CKEditor with django-ckeditor-updated (https://github.com/riklaunim/django-ckeditor) and some borrowed code from https://gist.github.com/elidickinson/1379652 to add the editor to the Flatpages admin.
