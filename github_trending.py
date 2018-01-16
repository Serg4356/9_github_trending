import requests
import datetime


def get_trending_repositories(top_size, search_date):
    request_params = {
        'q': 'created:>{}'.format(search_date),
        'sort': 'stars',
        'order': 'desc'
    }
    github_response = requests.get(
        'https://api.github.com/search/repositories',
        request_params
    )
    print(github_response.url)
    return github_response.json()['items'][:top_size]


def get_open_issues_amount(repo_owner, repo_name):
    github_response = requests.get(
        'https://api.github.com/repos/{}/{}/issues'.format(repo_owner, repo_name)
    )
    return github_response.json()


def get_days_passed(days):
    return (datetime.datetime.today() - datetime.timedelta(days=days)).strftime('%Y-%m-%d')


if __name__ == '__main__':
    top_size = 1
    period = 7
    print('Top {} trending repositories on Github:'.format(top_size))
    for repository in get_trending_repositories(top_size, get_days_passed(period)):
        print('{}, stars: {}, issues: {}, link: {}'.format(
            repository['name'],
            repository['stargazers_count'],
            len(get_open_issues_amount(
                repository['owner']['login'],
                repository['name']
            )),
            repository['html_url']
        ))
