from django.test import TestCase
from django.contrib.auth.models import User

from words.models import Entry

class EntryTestCase(TestCase):
	def setUp(self):
		test_user = User.objects.create_user('Fakey Fakerson', 'fake@test.com', 'notreal')
		self.test_entry = Entry.objects.create(
			title='This is a test entry.',
			author=test_user,
			text='This is the body of the test entry. Not a whole lot here.'
		)

	def test_string_representation(self):
		self.assertEqual(str(self.test_entry),'This is a test entry.')

	def test_slugify(self):
		self.assertEqual(self.test_entry.slug, 'this-is-a-test-entry')