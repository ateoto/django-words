"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from . import models

class EntryAdmin(SummernoteModelAdmin):

	def save_model(self, request, obj, form, change):
		if not obj.id:
			obj.author = request.user
		
		obj.save()


admin.site.register(models.Entry, EntryAdmin)
"""