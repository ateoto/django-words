from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Entry(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(User)
	published_on = models.DateTimeField(auto_now_add=True)
	text = models.TextField()
	slug = models.SlugField()

	def __str__(self):
		return self.title
	
	def save(self, *args, **kwargs):
		if not self.pk and not self.slug:
			self.slug = slugify(self.title)

		super(Entry, self).save(*args, **kwargs)
