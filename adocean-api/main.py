import requests
import json
import os


class AdOcean:
    def __init__(self, login, password):
        self.login_payload = {
            'login': login,
            'passwd': password
        }
        self.base_url = 'https://api.adocean.pl/json'
        self.session = requests.session()
        self._session_id = None

    def open_session(self):
        login_request = self.post('OpenSession', payload=self.login_payload)
        session_response = json.loads(login_request.text)
        if session_response['OpenSession']['status'] != 'OK':
            raise Exception(session_response)
        else:
            session_id = session_response['OpenSession']['sessionID']
        self.session_id = {'sessionID': session_id}


    def close_session(self):
        return self.post('CloseSession')

    def get(self, path, params=None):
        print(params)
        return self._build('GET', path, params=params)

    def post(self, path, payload=None):
        print(payload)
        return self._build('POST', path, payload)

    # TODO decorator error handling
    def _build(self, method, path, payload=None, params=None):
        if path != 'OpenSession':
            if params is None:
                params = self._session_id
            else:
                params.update(self.session_id)

        url = '{}/{}.php'.format(
            self.base_url, path)
        response = self.session.request(method, url, data=payload, params=params)
        print(response.url)
        return response
