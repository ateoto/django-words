from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


@python_2_unicode_compatible
class Entry(models.Model):
    title = models.CharField(max_length=200, unique_for_date='published_on')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)
    published_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    text = RichTextField()
    slug = models.SlugField(editable=False)

    tags = TaggableManager()

    class Meta:
        verbose_name_plural = 'Entries'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.pk and not self.slug:
            self.slug = slugify(self.title)

        super(Entry, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('entry-detail', kwargs={
            'year': self.published_on.year,
            'month': self.published_on.month,
            'day': self.published_on.day, 
            'slug': str(self.slug)
        })
