import requests
import datetime as dt

# Constants
#API_BASE_URL = "https://py-test-02-iis:8443"
API_BASE_URL = "https://api.py.energy"
SESSION_TIMEOUT_MINUTES = 1

# Proxy authentification
def get_session():
    """Create a new session with proxy authentication."""
    session = requests.Session()
    #session.verify = False  # for the test system, the verification of the session must be set to False, otherwise no session can be created
    session.proxies = {'http': 'http://proxy.enertrag.de:3128', 'https': 'http://proxy.enertrag.de:3128'}
    return session

class Masterdata:
    def __init__(self):        
        self._last_refresh = None
        self._session = None
        self.token = None   

    def session(self):
        now = dt.datetime.now()
        if (self._last_refresh is None) or (self._last_refresh < now - dt.timedelta(minutes = SESSION_TIMEOUT_MINUTES)):
            self._session = get_session()
            self._last_refresh = now
        return self._session

    def get_auth_token(self, username, password):
        api_auth_url = f"{API_BASE_URL}/auth/user"
        credentials = {"username": username, "password": password}
        try:
            response = self.session().post(api_auth_url, data=credentials)
            response.raise_for_status()
            self.token = response.json().get("access_token")
            return self.token
        except requests.exceptions.RequestException as e:
            print(f"API request error:\n{e}")  

        

    def get_installations(self, token):
        
        api_url = f"{API_BASE_URL}/masterdata/installations/types?count=1000&offset=0"
        

        try:
            headers = {
                "Authorization": f"Bearer {token}"
                }
            response = self.session().get(api_url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API request error:\n{e}")        

 



       
