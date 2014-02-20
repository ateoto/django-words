from django.test import LiveServerTestCase
from django.test.client import Client
from django.contrib.auth.models import User

from selenium import webdriver

from words.models import Entry


class NewVisitorTest(LiveServerTestCase):
	@classmethod
	def setUpClass(cls):
		cls.browser = webdriver.Firefox()
		cls.browser.implicitly_wait(3)
		super(NewVisitorTest, cls).setUpClass()

	@classmethod
	def tearDownClass(cls):
		cls.browser.quit()

	def setUp(self):
		self.client = Client()
		test_user = User.objects.create_superuser('fakey', 'fake@test.com', 'notreal')
		self.test_entry = Entry.objects.create(
			title='This is a test entry.',
			author=test_user,
			text='This is the body of the test entry. Not a whole lot here.'
		)

		Entry.objects.create(
			title='Another test.',
			author=test_user,
			text='How does TWO sound?'
		)

	def test_login_real(self):
		self.browser.get('%s%s' % (self.live_server_url, '/admin/'))
		self.browser.find_elements_by_css_selector('#id_username')[0].send_keys('fakey')
		self.browser.find_elements_by_css_selector('#id_password')[0].send_keys('notreal')
		self.browser.find_element_by_xpath('//input[@value="Log in"]').click()
		self.assertTrue(self.browser.find_element_by_css_selector('#user-tools').is_displayed())

	def test_index(self):
		with self.assertTemplateUsed('words/entry_list.html'):
			response = self.client.get('/blog/')
			self.assertEqual(response.status_code, 200)
			self.assertEqual(len(response.context['object_list']), 2)

	def test_index_live(self):
		self.browser.get('%s%s' % (self.live_server_url, '/blog/'))

		entries_html = self.browser.find_elements_by_tag_name('h4')

		for entry in Entry.objects.all():
			self.assertTrue(
				any(entry_html.text == entry.title for entry_html in entries_html)
			)

	def test_unauth_cant_see_entry_add(self):
		response = self.client.get('/blog/add/')
		self.assertEqual(response.status_code, 302)

	def test_can_see_entry_add(self):
		self.client.login(username='fakey', password='notreal')

		with self.assertTemplateUsed('words/entry_form.html'):
			response = self.client.get('/blog/add/')
			self.assertEqual(response.status_code, 200)

	def test_can_add_entry(self):
		self.client.login(username='fakey', password='notreal')
		
		with self.assertTemplateUsed('words/entry_detail.html'):
			response = self.client.post('/blog/add/', {'title': 'Test Title', 'text': 'The test text.', 'tags': 'TestTag'}, follow=True)
			self.assertEqual(response.status_code, 200)

	def test_entry_view(self):
		with self.assertTemplateUsed('words/entry_detail.html'):
			response = self.client.get(self.test_entry.get_absolute_url())
			self.assertEqual(response.status_code, 200)
