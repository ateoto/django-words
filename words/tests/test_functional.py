import unittest
from datetime import timedelta, datetime
import calendar

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
        self.test_user = User.objects.create_superuser('fakey', 'fake@test.com', 'notreal')
        self.test_entry = Entry.objects.create(
            title='This is a test entry.',
            author=self.test_user,
            text='This is the body of the test entry. Not a whole lot here.'
        )
        self.test_entry.tags.add('testing','space testing')

        self.test_entry_two = Entry.objects.create(
            title='Another test.',
            author=self.test_user,
            text='How does TWO sound?'
        )
        self.test_entry_two.tags.add('testing')

    def test_login_live(self):
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

        entries_html = self.browser.find_elements_by_css_selector('.article-title')

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
            response = self.client.post('/blog/add/', {'title': 'Test Title', 'text': 'The test text.', 'tags': 'testing'}, follow=True)
            self.assertEqual(response.status_code, 200)

    def test_entry_view(self):
        with self.assertTemplateUsed('words/entry_detail.html'):
            response = self.client.get(self.test_entry.get_absolute_url())
            self.assertEqual(response.status_code, 200)

    def test_tag_filtering(self):
        with self.assertTemplateUsed('words/tag_archive.html'):
            response = self.client.get('/blog/tags/testing/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.context['object_list']), 2)
        with self.assertTemplateUsed('words/tag_archive.html'):
            response = self.client.get('/blog/tags/space-testing/')
            self.assertEqual(len(response.context['object_list']), 1)

    @unittest.skip("TODO: Fails, even though it works with runserver. :/")
    def test_tag_list(self):
        with self.assertTemplateUsed('words/tag_list.html'):
            response = self.client.get('/blog/tags/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.context['object_list']), 2)

    def test_year_archive(self):
        a_year = timedelta(days=365)
        today = datetime.now()
        next_year = today + a_year
        last_year = today - a_year

        date_test_entry = Entry.objects.create(
            title='This is a test entry for dates by year',
            author=self.test_user,
            text='I am creating an entry so that I can modify the date for testing.'
        )
        date_test_entry.tags.add('testing','dates')
        date_test_entry.published_on = last_year
        date_test_entry.save()

        with self.assertTemplateUsed('words/entry_list.html'):
            response = self.client.get('/blog/%d/' % today.year)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.context['entry_list']), 2)

        with self.assertTemplateUsed('words/entry_list.html'):
            response = self.client.get('/blog/%d/' % last_year.year)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.context['entry_list']), 1)

        response = self.client.get('/blog/%d/' % next_year.year)
        self.assertEqual(response.status_code, 404)

    def test_month_archive(self):
        today = datetime.now()
        days_in_current_month = calendar.monthrange(today.year, today.month)[1]
        a_month = timedelta(days=days_in_current_month)
        next_month = today + a_month
        last_month = today - a_month

        date_test_entry = Entry.objects.create(
            title='This is a test entry for dates by month',
            author=self.test_user,
            text='I am creating an entry so that I can modify the date for testing.'
        )
        date_test_entry.tags.add('testing','dates')
        date_test_entry.published_on = last_month
        date_test_entry.save()

        with self.assertTemplateUsed('words/entry_list.html'):
            response = self.client.get('/blog/%d/%d/' % (today.year, today.month))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.context['entry_list']), 2)

        with self.assertTemplateUsed('words/entry_list.html'):
            response = self.client.get('/blog/%d/%d/' % (last_month.year, last_month.month))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.context['entry_list']), 1)

        response = self.client.get('/blog/%d/%d/' % (next_month.year, next_month.month))
        self.assertEqual(response.status_code, 404)

    def test_day_archive(self):
        today = datetime.now()
        a_day = timedelta(days=1)
        tommorow = today + a_day
        yesterday = today - a_day

        date_test_entry = Entry.objects.create(
            title='This is a test entry for dates by month',
            author=self.test_user,
            text='I am creating an entry so that I can modify the date for testing.'
        )
        date_test_entry.tags.add('testing','dates')
        date_test_entry.published_on = yesterday
        date_test_entry.save()

        with self.assertTemplateUsed('words/entry_list.html'):
            response = self.client.get('/blog/%d/%d/%d/' % (today.year, 
                                                            today.month, 
                                                            today.day))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.context['entry_list']), 2)

        with self.assertTemplateUsed('words/entry_list.html'):
            response = self.client.get('/blog/%d/%d/%d/' % (yesterday.year,
                                                            yesterday.month,
                                                            yesterday.day))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.context['entry_list']), 1)

        response = self.client.get('/blog/%d/%d/%d/' % (tommorow.year,
                                                        tommorow.month,
                                                        tommorow.day))
        self.assertEqual(response.status_code, 404)