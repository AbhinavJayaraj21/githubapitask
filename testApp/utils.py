import requests

def search_github_repositories(query):
    url = f"https://api.github.com/search/repositories?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['items']
    else:
        return None
