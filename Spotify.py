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


all_playlist_songs = {}

for playlist in playlists['playlists']['items']:
    playlist_id = playlist['id']
    playlist_name = playlist['name']
    print(f"Fetching songs from playlist: {playlist_name}")


    tracks_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    tracks_response = requests.get(tracks_url, headers=headers)
    tracks_data = tracks_response.json()


    songs = []
    for item in tracks_data['items']:
        track = item['track']
        if track:
            song_name = track['name']
            artist_name = ', '.join([artist['name'] for artist in track['artists']])
            songs.append({'song_name': song_name, 'artist': artist_name})


    all_playlist_songs[playlist_name] = songs


    all_playlist_songs[playlist_name] = songs


with open('guilty_pleasures_songs.json', 'w') as f:
    json.dump(all_playlist_songs, f, indent=2)


for playlist_name, songs in all_playlist_songs.items():
    print(f"\nPlaylist: {playlist_name}")
    for song in songs:
        print(f"- {song['song_name']} by {song['artist']}")


