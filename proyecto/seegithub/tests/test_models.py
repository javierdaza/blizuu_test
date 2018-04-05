from django.test import TestCase

from seegithub.models import Repository


class TestRepository(TestCase):

    def setUp(self):
        self.repo = Repository.objects.create(
            github_id=123245,
            name='Example Repository',
            htme_url='http://example.com/',
            description = 'Short description',
            created_at='2013-03-29T18:38:45Z',
            last_commit='{"menu":{"id":"file","value":"File","popup":{"menuitem":[{"value":"New","onclick":"CreateNewDoc()"},{"value":"Open","onclick":"OpenDoc()"},{"value":"Close","onclick":"CloseDoc()"}]}}}',
        )

    def test_github_id(self):
        self.assertEqual(
            self.repo.github_id,
            123245
        )

    def test_name(self):
        self.assertEqual(self.repo.name, 'Example Repository')

    def test_htme_url(self):
        self.assertEqual(self.repo.htme_url, 'http://example.com/')

    def test_description(self):
        self.assertEqual(self.repo.description, 'Short description')

    def test_created_at(self):
        self.assertEqual(self.repo.created_at, '2013-03-29T18:38:45Z')

    def test_last_commit(self):
        self.assertEqual(self.repo.last_commit, '{"menu":{"id":"file","value":"File","popup":{"menuitem":[{"value":"New","onclick":"CreateNewDoc()"},{"value":"Open","onclick":"OpenDoc()"},{"value":"Close","onclick":"CloseDoc()"}]}}}')


class RepositoryModelTest(TestCase):

    def test_string_representation(self):
        repo = Repository(name="My name")
        self.assertEqual(str(repo), repo.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Repository._meta.verbose_name_plural), "Repositories")

