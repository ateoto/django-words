from django.contrib import admin

from . import models


class EntryAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.author = request.user
        
        obj.save()


admin.site.register(models.Entry, EntryAdmin)