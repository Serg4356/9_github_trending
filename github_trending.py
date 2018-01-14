import requests
import json
import datetime


def get_trending_repositories(top_size):
    request_params = 'q=created:>={}&sort=stars&order=desc'.format(str(get_days_passed())[0:10])
    github_request = requests.get(
        'https://api.github.com/search/repositories',
        request_params
    )
    github_request_json = github_request.json()
    return github_request_json['items'][0:top_size]


def get_days_passed():
    return datetime.datetime.today() - datetime.timedelta(days=7)


if __name__ == '__main__':
    top_size = 20
    print('Top {} trending repositories on Github:'.format(top_size))
    for repository in get_trending_repositories(top_size):
        print('{}, stars: {}, issues: {}, link: {}'.format(
            repository['name'],
            repository['stargazers_count'],
            repository['open_issues_count'],
            repository['html_url']
        ))
