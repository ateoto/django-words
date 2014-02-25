from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import (EntryList, EntryCreate, EntryDetail, TagList, TagArchive,
					EntryYearArchive, EntryMonthArchive, EntryDayArchive)


urlpatterns = patterns('',
    url(r'^$', EntryList.as_view(), name='entry-list'), 
    url(r'^page/(?P<page>\d+)/$', EntryList.as_view(), name='paginated-entry-list'),
    url(r'^add/$', login_required(EntryCreate.as_view()), name='entry-add'),
    url(r'^tags/$', TagList.as_view(), name='tag-list'),
	url(r'^tags/(?P<tag_slug>[-\w]+)/$', TagArchive.as_view(), name='tag-archive'),
	url(r'^(?P<year>\d+)/$', EntryYearArchive.as_view(), name='entry-year-archive'),
	url(r'^(?P<year>\d{4})/(?P<month>\d+)/$', EntryMonthArchive.as_view(month_format='%m'), name='entry-month-archive'),
	url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/$', EntryDayArchive.as_view(month_format='%m'), name='entry-day-archive'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[-\w]+)/$', EntryDetail.as_view(), name='entry-detail'),
)
