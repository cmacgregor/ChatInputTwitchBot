import requests

#this should be made async
def fetch_oath_access_token(client_id:str, client_secret:str) -> str:
    endpoint = 'https://id.twitch.tv/oauth2/token'

    parameters = {'client_id': client_id, 'client_secret': client_secret, 'grant_type': 'client_credentials' } 

    response = requests.post(url=endpoint, params=parameters)

    response_json = response.json()

    return response_json['access_token']