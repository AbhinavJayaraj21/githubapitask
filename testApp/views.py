from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Repository
from .utils import search_github_repositories


# Create your views here.


def home(request):
    return render(request, 'home.html')


def search(request):
    query = request.GET.get('query')
    if query:
        repositories = search_github_repositories(query)
        if repositories:
            # Save searched repositories to the database
            for repo_data in repositories:
                repo = Repository(
                    name=repo_data['name'],
                    owner=repo_data['owner']['login'],
                    description=repo_data['description'],
                    stars=repo_data['stargazers_count'],
                    forks=repo_data['forks_count']
                )
                repo.save()

            # Paginate search results
            paginator = Paginator(repositories, 10)
            page = request.GET.get('page')
            try:
                repositories = paginator.page(page)
            except PageNotAnInteger:
                repositories = paginator.page(1)
            except EmptyPage:
                repositories = paginator.page(paginator.num_pages)

            return render(request, 'search_results.html', {'repositories': repositories})
        else:
            return render(request, 'search_results.html', {'error_message': 'No repositories found.'})
    else:
        return render(request, 'home.html', {'error_message': 'Please enter a search query.'})
