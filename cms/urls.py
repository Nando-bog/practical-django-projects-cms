#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^files/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^search/$', 'search.views.search'),
    url(r'^home', 'search.views.home'),
    url(r'^index', 'search.views.home'),
    (r'^$', 'search.views.home'),
    (r'^weblog/$', 'coltrane.views.entries_index'),
    #(r'^weblog/2013/12/28/testing-1/$', 'coltrane.views.entry_detail'),
    (r'^weblog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/{0,1}$', 'coltrane.views.entry_detail'),
    #(r'', include('django.contrib.flatpages.urls')),
)