#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.dates import DateDetailView, YearArchiveView, MonthArchiveView, DayArchiveView
from django.conf import settings
from django.conf.urls.static import static
from coltrane.models import Entry

admin.autodiscover()

entry_info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}

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
    url(r'^weblog/$', 'coltrane.views.entries_index'),    #(r'^weblog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/{0,1}$', 'coltrane.views.entry_detail'),
    #(r'', include('django.contrib.flatpages.urls')),
    url(r'^weblog/(?P<year>\d{4})/{0,1}$', YearArchiveView.as_view(model=Entry, date_field="pub_date", make_object_list = True)),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\d{2})/{0,1}$', MonthArchiveView.as_view(model=Entry, date_field="pub_date", month_format="%m")),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/{0,1}$', DayArchiveView.as_view(model=Entry, date_field="pub_date", month_format="%m", allow_future=True)),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/{0,1}$', DateDetailView.as_view(model=Entry, date_field="pub_date", month_format="%m", allow_future=True)),
)