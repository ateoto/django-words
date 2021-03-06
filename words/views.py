from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.dates import YearArchiveView, MonthArchiveView, DayArchiveView
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from .models import Entry
from .forms import EntryForm


class EntryList(ListView):
	context_object_name = "entry_list"
	queryset = Entry.objects.filter(published=True).order_by("-published_on")
	paginate_by = 5

class EntryYearArchive(YearArchiveView):
	context_object_name = "entry_list"
	queryset = Entry.objects.filter(published=True).order_by("-published_on")
	date_field = "published_on"
	make_object_list = True
	template_name = "words/entry_list.html"

class EntryMonthArchive(MonthArchiveView):
	context_object_name = "entry_list"
	queryset = Entry.objects.filter(published=True).order_by("-published_on")
	date_field = "published_on"
	make_object_list = True
	template_name = "words/entry_list.html"

class EntryDayArchive(DayArchiveView):
	context_object_name = "entry_list"
	queryset = Entry.objects.filter(published=True).order_by("-published_on")
	date_field = "published_on"
	make_object_list = True
	template_name = "words/entry_list.html"

class EntryDetail(DetailView):
	model = Entry

class EntryCreate(CreateView):
	form_class = EntryForm
	template_name = "words/entry_form.html"

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(EntryCreate, self).form_valid(form)

class TagList(ListView):
	queryset = Entry.tags.most_common()
	template_name = "words/tag_list.html"

class TagArchive(ListView):
	template_name = "words/tag_archive.html"

	def get_queryset(self):
		return Entry.objects.filter(published=True).filter(
			tags__slug__in=[self.kwargs['tag_slug']]
		).order_by('-published_on')

	def get_context_data(self, **kwargs):
		context = super(TagArchive, self).get_context_data(**kwargs)
		context['tag'] = get_object_or_404(Entry.tags, slug=self.kwargs['tag_slug'])
		return context