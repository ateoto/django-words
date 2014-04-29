from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from . import models


def make_published(modeladmin, request, queryset):
    queryset.update(published=True)
make_published.short_description = "Mark selected stories as published"


class EntryAdmin(SummernoteModelAdmin):
    list_display = ('title', 'published')
    actions = [make_published]
    
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.author = request.user
        
        obj.save()


admin.site.register(models.Entry, EntryAdmin)