from django.test import TestCase


from seegithub.models import Repository


class TestRepositoryViews(TestCase):

    def setUp(self):
        self.repo = Repository.objects.create(
            github_id=123245,
            name='Example Repository',
            htme_url='http://example.com/',
            description = 'Short description',
            created_at='2013-03-29T18:38:45Z',
            last_commit='{"menu":{"id":"file","value":"File","popup":{"menuitem":[{"value":"New","onclick":"CreateNewDoc()"},{"value":"Open","onclick":"OpenDoc()"},{"value":"Close","onclick":"CloseDoc()"}]}}}',
        )

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_save_repos(self):
        response = self.client.get('/save_repos')
        self.assertEqual(response.status_code, 302)

    def test_listfromdb(self):
        resp = self.client.get('/list')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['repoItem']), 1)

    def test_ordered_by_date(self):
        response = self.client.get('/ordered_by_date')
        self.assertEqual(response.status_code, 200)

    def test_orderded_by_commit(self):
        response = self.client.get('/ordered_by_commit')
        self.assertEqual(response.status_code, 200)
