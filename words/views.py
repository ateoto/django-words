from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

from .models import Entry
from .forms import EntryForm


class LatestEntryList(ListView):
    context_object_name = "entry_list"
    queryset = Entry.objects.order_by("-published_on")

class EntryDetail(DetailView):
	model = Entry


class EntryCreate(CreateView):
	form_class = EntryForm
	template_name = "words/entry_form.html"

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(EntryCreate, self).form_valid(form)

class TagArchive(ListView):
	template_name = "words/tag_archive.html"

	def get_queryset(self):
		return Entry.objects.filter(
			tags__slug__in=[self.kwargs['tag_slug']]
		).order_by('-published_on')

	def get_context_data(self, **kwargs):
		context = super(TagArchive, self).get_context_data(**kwargs)
		context['tag'] = get_object_or_404(Entry.tags, slug=self.kwargs['tag_slug'])
		return context