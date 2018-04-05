import requests
import json

from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.core.urlresolvers import reverse
from django.template import Context

from .models import Repository


def save_repos(request):
    repos = requests.get('https://api.github.com/orgs/githubtraining/repos')
    if (repos.ok):
        repoItem = json.loads(repos.text or repos.content)
        # Last 10 repos in Github
        for counter in range(0, len(repoItem)):
            if counter >= len(repoItem) - 10:
                base_url = 'https://api.github.com/repos/githubtraining/'
                commits_url = base_url + str(repoItem[counter]['name']) + '/commits'
                list_of_commits = requests.get(commits_url)
                listItem = json.loads(list_of_commits.text or list_of_commits.content)
                repo = Repository.objects.create(github_id=repoItem[counter]['id'], name=repoItem[counter]['name'], htme_url=repoItem[counter]['html_url'], description = repoItem[counter]['description'], created_at=repoItem[counter]['created_at'], last_commit=listItem[0])
        messages.success(request, "La base de datos fue cargada exitosamente")
    else:
        messages.warning(request, "Hubo un problema haciendo el request a la API de Github")
    
    return HttpResponseRedirect(reverse('index'))

def index(request):
    repos = requests.get('https://api.github.com/orgs/githubtraining/repos')

    if (repos.ok):
        repoItem = json.loads(repos.text or repos.content)
    else:
        repoItem = Repository.objects.all()
    data = {
        'repoItem': repoItem,
    }
    return render(request, "seegithub/index.html", data)


def order_by_date(request):
    repos = requests.get('https://api.github.com/orgs/githubtraining/repos')
    if (repos.ok):
        repoItem = json.loads(repos.text or repos.content)
    else:
        repoItem = Repository.objects.all()
    data = {
        'repoItem': repoItem,
    }
    return render(request, "seegithub/ordered_by_date.html", data)

def ordered_by_commit(request):
    repos = requests.get('https://api.github.com/orgs/githubtraining/repos')
    if (repos.ok):
        repoItem = json.loads(repos.text or repos.content)
        base_url = 'https://api.github.com/repos/githubtraining/'
        commits_url = base_url + str(repoItem[0]['name']) + '/commits'
        list_of_commits = requests.get(commits_url)
        listItem = json.loads(list_of_commits.text or list_of_commits.content)
    else:
        repoItem = Repository.objects.all()
        repo_context = repoItem
    
    if (repos.ok):
        repo_context = Context({"id": repoItem[0]['id'], "html_url": repoItem[0]['html_url'],"name": repoItem[0]['name'],"created_at": repoItem[0]['created_at'], "sha": listItem[0]['sha'], "commit_url": listItem[0]['html_url'], "date_commit": listItem[0]['commit']['committer']['date']})
        for counter in range(1, 18):
            repo_context.push({"id": repoItem[counter]['id'], "html_url": repoItem[counter]['html_url'],"name": repoItem[counter]['name'],"created_at": repoItem[counter]['created_at'], "sha": listItem[counter]['sha'], "commit_url": listItem[counter]['html_url'], "date_commit": listItem[counter]['commit']['committer']['date']})
    data = {
        'repoItem': repo_context,
    }
    return render(request, "seegithub/ordered_by_commit.html", data)

def search_repo(request):
    search_item = str(request.POST['search_item'])
    repos = requests.get('https://api.github.com/orgs/githubtraining/repos')
    if (repos.ok):
        repoItem = json.loads(repos.text or repos.content)

        for counter in range(0, len(repoItem)):
            if search_item in repoItem[counter]['name']:
                print(counter)
                if counter == 0:
                    repo_context = Context({"id": repoItem[0]['id'], "html_url": repoItem[0]['html_url'],"name": repoItem[0]['name'],"created_at": repoItem[0]['created_at'] }) 
                else:
                    try:
                        repo_context.push({"id": repoItem[counter]['id'], "html_url": repoItem[counter]['html_url'],"name": repoItem[counter]['name'],"created_at": repoItem[counter]['created_at'] })
                    except UnboundLocalError:
                        repo_context = Context({"id": repoItem[counter]['id'], "html_url": repoItem[counter]['html_url'],"name": repoItem[counter]['name'],"created_at": repoItem[counter]['created_at'] })                 
    data = {
        'repoItem': repo_context,
    }
    return render(request, "seegithub/search_repo.html", data)


class ListFromDb(generic.ListView):
    template_name = 'seegithub/list.html'
    context_object_name = 'repoItem'
    model = Repository
        
