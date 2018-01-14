import requests
import json
import datetime


def get_trending_repositories(top_size, search_date):
    request_params = {'q': {
        'created>': search_date,
        'sort': 'stars',
        'order': 'desc'
    }}
    github_response = requests.get(
        'https://api.github.com/search/repositories',
        request_params
    )
    return github_response.json()['items'][:top_size]


def get_open_issues_amount(repo_owner, repo_name):
    github_response = requests.get(
        'https://api.github.com/repos/{}/{}/issues'.format(repo_owner, repo_name)
    )
    return github_response.json()


def get_days_passed():
    return datetime.datetime.today() - datetime.timedelta(days=7)


if __name__ == '__main__':
    top_size = 20
    print('Top {} trending repositories on Github:'.format(top_size))
    for repository in get_trending_repositories(top_size, str(get_days_passed())[:10]):
        print('{}, stars: {}, issues: {}, link: {}'.format(
            repository['name'],
            repository['stargazers_count'],
            len(get_open_issues_amount(
                repository['owner']['login'],
                repository['name']
            )),
            repository['html_url']
        ))
