import requests
import re


class GitHubClient:
    def __init__(self, api_token):
        self.api_token = api_token
        self.auth_headers = {'Authorization': 'token {}'.format(self.api_token)}
        
        self.api_root = 'https://api.github.com'
        self.api_repo = self.api_root + '/repos/{}/{}'
        self.api_branches = self.api_repo + '/branches'
        self.api_tags = self.api_repo + '/tags'
        self.api_pulls = self.api_repo + '/pulls'
        self.api_compare = self.api_repo + '/compare/{base}...{head}'

    def _get(self, uri, paginated=False, page_size=100, max_pages=100, querystring=None):
        _querystring = querystring.copy() if querystring else {}
        if paginated:
            _querystring['per_page'] = page_size

        response = requests.get(
            uri, params=_querystring,
            headers=self.auth_headers
        )
        if not paginated:
            return response.json()

        results = [response.json()]
        pages = 1
        while pages < max_pages:
            pages += 1
            response = requests.get(
                uri, params=_querystring,
                headers=self.auth_headers
            )
            page_of_results = response.json()
            if not page_of_results:
                break
            results.extend(page_of_results)
            if not isinstance(page_of_results, list):
                results = page_of_results
            if 'Link' not in response.headers:
                break
            links = GitHubClient.decompose_link_header(response.headers.get('Link'))
            if 'next' not in links:
                break
            uri = links.get('next')
        if pages == max_pages:
            print("WARNING: max_pages of {} exceeded.".format(max_pages))
        return results

    @staticmethod
    def decompose_link_header(header):
        """
        Turns:
            <https://api.github.com/repositories/4864368/branches?page=2>; rel="next",
            <https://api.github.com/repositories/4864368/branches?page=8>; rel="last"
        Into:
            {'next': 'https://api.github.com/repositories/4864368/branches?page=2',
             'last': 'https://api.github.com/repositories/4864368/branches?page=8'}
        """
        m = re.findall('([<]([^>]+)[>]; rel="(\w+)")+', header)
        return {x[2]: x[1] for x in m}
    
    def get_branches(self, account, repo):
        return self._get(self.api_branches.format(account, repo), paginated=True)
    
    def get_tags(self, account, repo):
        return self._get(self.api_tags.format(account, repo), paginated=True)
    
    def get_pulls(self, account, repo):
        return self._get(self.api_pulls.format(account, repo), paginated=True)

    def get_compare(self, account, repo, base, head):
        return self._get(self.api_compare.format(account, repo, base=base, head=head))