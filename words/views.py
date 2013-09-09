from django.views.generic import ListView
from .models import Entry

class LatestEntryList(ListView):
    model = Entry