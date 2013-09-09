from django.conf.urls import patterns, url
from .views import LatestEntryList

urlpatterns = patterns('',
    url(r'^$', LatestEntryList.as_view()),
)