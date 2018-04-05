from django.core.urlresolvers import reverse, resolve
from django.test import TestCase


class TestURLs(TestCase):
    """Test the URL patterns"""

    def test_urls(self):
        self.assertEqual(reverse('index'), '/')
        self.assertEqual(reverse('save_repos'), '/save_repos')
        self.assertEqual(reverse('order_by_date'), '/ordered_by_date')
        self.assertEqual(reverse('ordered_by_commit'), '/ordered_by_commit')
        self.assertEqual(reverse('search_repo'), '/search_repo')
        self.assertEqual(reverse('list'), '/list')