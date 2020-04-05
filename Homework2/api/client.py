from urllib.parse import urljoin

import requests
import json


class ResponseStatusCodeException(Exception):
    pass


class ApiClient:

    def __init__(self, user, password):
        self.base_url = 'https://target.my.com/'

        self.session = requests.Session()
        self.user = user
        self.password = password

    def _request(self, method, location, headers=None, params=None, data=None, json=False, redirect=False):
        url = urljoin(self.base_url, location)

        response = self.session.request(method, url, headers=headers, params=params, data=data, allow_redirects=redirect)

        if json:
            response = response.json()

        return response

    def redir_auth(self, user, password):
        location = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'
        data = {
            'email': user,
            'password': password,
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            'Referer': 'https://target.my.com/'
        }
        headers = self._request('POST', location, data=data, headers=headers).headers
        return headers['Location']

    def auth(self):

        location = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'
        data = {
            'email': self.user,
            'password': self.password,
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            'Referer': 'https://target.my.com/'
        }
        headers = self._request('POST', location, data=data, headers=headers).headers
        Cookie = headers['Set-Cookie'].split(';')
        mc = Cookie[0]
        ssdc = Cookie[7].split()[1]
        mrcu = Cookie[14].split()[1]
        return f'{mc}; {ssdc}; {mrcu}'

    def get_z(self):
        location = 'https://target.my.com/api/v2/localization_components.json?lang=en,ru'
        headers = self._request('GET', location).headers
        return headers['Set-Cookie'].split(';')[0]

    def redirect(self):
        location = 'https://target.my.com/auth/mycom?state=target_login%3D1#email'
        headers = {
            'Cookie': f'{self.get_z()}; {self.auth()}'
        }
        redirect = self._request('GET', location, headers=headers).headers['Location']
        return {'headers': headers, 'Location': redirect}

    def ssdc(self):
        data = self.redirect()
        location = data['Location']
        headers = data['headers']
        redirect = self._request('GET', location, headers=headers).headers['Location']
        return {'headers': headers, 'Location': redirect}

    def sdcs(self):
        data = self.ssdc()
        location = data['Location']
        headers = data['headers']
        response_head = self._request('GET', location, headers=headers).headers
        sdcs = response_head['Set-Cookie'].split(';')[0]
        headers['Cookie'] += f'; {sdcs}'
        redirect = response_head['Location']
        return headers

    def csrf(self):
        location = 'https://target.my.com/csrf/'
        headers = self.sdcs()
        head = self._request('GET', location, headers).headers
        headers['Cookie'] += f'; {head["Set-Cookie"]}'
        return headers

    def login(self):
        self.headers = self.csrf()

    def create_segmentum(self, data):
        location = 'https://target.my.com/api/v2/remarketing/segments.json?fields=relations__object_type,relations__object_id,relations__params,relations_count,id,name,pass_condition,created,campaign_ids,users,flags'
        data = json.dumps(data)
        headers = {
            'Content-Type': 'application/json',
            'Cookie': self.headers['Cookie'],
            'Referer': 'https://target.my.com/segments/segments_list/new',
            'X-CSRFToken': self.headers['Cookie'].split(';')[5].split('=')[-1],
            'X-Requested-With': 'XMLHttpRequest'
        }
        return self._request('POST', location, headers=headers, data=data)

    def delete_segmentum(self, id):
        location = 'https://target.my.com/api/v2/remarketing/segments/' + f'{id}.json'
        headers = {
            'Cookie': self.headers['Cookie'],
            'Referer': 'https://target.my.com/segments/segments_list',
            'X-CSRFToken': self.headers['Cookie'].split(';')[5].split('=')[-1]
        }
        return self._request("DELETE", location, headers=headers).status_code
        