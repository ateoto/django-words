from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from .models import Entry
from .forms import EntryForm


class LatestEntryList(ListView):
    model = Entry


class EntryDetail(DetailView):
	model = Entry


class EntryCreate(CreateView):
	form_class = EntryForm
	template_name = "words/entry_form.html"

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(EntryCreate, self).form_valid(form)
