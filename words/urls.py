from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .views import (LatestEntryList, EntryCreate, 
					EntryDetail, TagArchive)


urlpatterns = patterns('',
    url(r'^$', LatestEntryList.as_view(), name='entry-list'), 
    url(r'^add/$', login_required(EntryCreate.as_view()), name='entry-add'),
	url(r'^tags/(?P<tag_slug>[-\w]+)/$', TagArchive.as_view(), name='tag-archive'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[-\w]+)/$', EntryDetail.as_view(), name='entry-detail'),
)
