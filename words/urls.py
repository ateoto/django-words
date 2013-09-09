from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import (LatestEntryList, EntryCreate)

urlpatterns = patterns('',
    url(r'^$', LatestEntryList.as_view()),
    url(r'^add/$', login_required(EntryCreate.as_view())),
)