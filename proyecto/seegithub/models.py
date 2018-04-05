from django.contrib.postgres.fields import JSONField
from django.db import models


class Repository(models.Model):
	'''
	Model for saving information about GitHub repositories
	'''
	github_id = models.BigIntegerField()
	name = models.CharField(max_length = 255)
	htme_url = models.URLField(max_length = 400)
	description = models.CharField(max_length = 400, null=True, blank=True)
	created_at = models.DateTimeField(help_text = "Date when this repository was created")
	last_api_consult = models.DateTimeField(auto_now_add = True)
	last_commit = JSONField()

	class Meta:
		verbose_name_plural = "Repositories"
		verbose_name = "Repository"
			
	def __str__(self):
		return self.name
