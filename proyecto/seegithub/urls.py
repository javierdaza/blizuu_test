from django.conf.urls import url
from django.contrib import admin

from seegithub import views

admin.site.site_header = 'Blizuu Test Administration'
admin.site.site_title = 'Blizuu Test Administration'


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^save_repos$', views.save_repos, name="save_repos"),
    url(r'^ordered_by_date$', views.order_by_date, name="order_by_date"),
    url(r'^ordered_by_commit$', views.ordered_by_commit, name="ordered_by_commit"),
    url(r'^search_repo$', views.search_repo, name="search_repo"),
    url(r'^list$', views.ListFromDb.as_view(), name="list"),
]