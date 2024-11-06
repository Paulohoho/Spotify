import requests


client_id = '80f0cb2bb9a04256bb11a2cfee9fff29'
client_secret = 'e5cd502777674ba1821af67cfe2117b6'


auth_url = 'https://accounts.spotify.com/api/token'
auth_response = requests.post(auth_url, {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
})
auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']


search_url = 'https://api.spotify.com/v1/search'
headers = {
    'Authorization': f'Bearer {access_token}'
}
params = {
    'q': 'guilty pleasures',
    'type': 'playlist',
    'limit': 20
}


response = requests.get(search_url, headers=headers, params=params)
playlists = response.json()


for playlist in playlists['playlists']['items']:
    print(playlist['name'], playlist['external_urls']['spotify'])

import json


with open('guilty_pleasures_playlists.json', 'w') as f:
    json.dump(playlists, f)




