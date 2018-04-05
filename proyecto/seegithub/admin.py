from django.contrib import admin

from .models import Repository


class RepositoryAdmin(admin.ModelAdmin):
	list_display = ("name", "github_id" , "created_at", "last_api_consult")

admin.site.register(Repository, RepositoryAdmin)
