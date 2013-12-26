#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('django.contrib.flatpages.urls')),
    #url(r'tiny_mce/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/static/tinymce/'}),
    (r'^ckeditor/', include('ckeditor.urls')),
)
