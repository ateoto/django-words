from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .views import (LatestEntryList, EntryCreate, EntryDetail)


urlpatterns = patterns('',
    url(r'^$', LatestEntryList.as_view(), name='entry-list'), 
    url(r'^add/$', login_required(EntryCreate.as_view()), name='entry-add'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[-\w]+)/$', EntryDetail.as_view(), name='entry-detail'),
)
