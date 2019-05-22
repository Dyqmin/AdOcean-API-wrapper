import requests
import json
import os


class AdOcean:
    def __init__(self, login, password, sesion_id=None):
        self.login = login
        self.password = password
        self.base_url = 'https://api.adocean.pl/json/'
        self.session = requests.session()
        self._sesion_id = sesion_id

    @property
    def session_id(self):
        """
        We are using textfile to hold sessionID.
        It helps us avoiding opening a new session every time.
        """
        session_file = 'sessionid.txt'

        mode = "r+" if os.path.isfile(session_file) else "w+"

        with open('sessionid.txt', mode=mode, encoding='utf-8') as f:
            f.seek(0)
            sesion_id = f.read()
            print(sesion_id)
            if sesion_id == "":
                sesion_id = self.open_session()
                f.write(sesion_id)
        return sesion_id

    def validate_session(func):
        def session_wrapper(*args, **kwargs):
            response = func(*args, **kwargs)
            if response['OpenSession']['status'] != 'OK':
                raise Exception(response)
            else:
                return response['OpenSession']['sessionID']
        return session_wrapper

    @validate_session
    def open_session(self):
        login_url = f'{self.base_url}OpenSession.php'
        login_request = self.session.post(
            login_url, data={'login': self.login, 'passwd': self.password})
        session_response = json.loads(login_request.text)
        return session_response

    def get(self, path, params=None):
        return self._build('GET', path, params=params)

    def post(self, path, payload=None):
        return self._build('POST', path, payload)

    # TODO decorator error handling
    def _build(self, method, path, payload=None, params=None):
        pass
