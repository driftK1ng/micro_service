import requests
from app.settings import settings

def auth(username: str, password: str):
    url = f'{settings.keycloak_url}/{settings.keycloak_realm}/protocol/openid-connect/token'
    data = {
    'username': username,
    'password': password,
    'client_id': settings.keycloak_id,
    'client_secret': settings.keycloak_secret,
    'grant_type': 'password',
    'scope': 'openid'
    }
    response = requests.post(url, data=data)

    return response

def check_token(token: str):
    header = {'Authorization': f'Bearer {token}'}
    url = f'{settings.keycloak_url}/{settings.keycloak_realm}/protocol/openid-connect/userinfo'

    response = requests.get(url=url, headers=header)

    return response

