#coding=utf-8
#CMS project URLS

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.dates import DateDetailView, YearArchiveView, MonthArchiveView, DayArchiveView
from django.conf import settings
from django.conf.urls.static import static
from coltrane.models import Entry

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
    url(r'^weblog/', include('coltrane.urls')),
)