import requests
from bs4 import BeautifulSoup
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime as dt

ID = "example1"
SECRET = "example2"
BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_URL = "https://open.spotify.com/"
REDIRECT_URL = "https://redurl.com/callback/"

user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
if user_date == "":
    user_date = dt.datetime.now()

response = requests.get(url=f"{BILLBOARD_URL}{user_date}")
soup = BeautifulSoup(response.text, "html.parser")
song_titles = soup.find_all(name="h3",
                            class_=re.compile("c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021"))
all_songs = [song.getText().strip() for song in song_titles]

print(all_songs)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=ID, client_secret=SECRET, redirect_uri=REDIRECT_URL,
                                               scope="playlist-modify-private", show_dialog=True,
                                               cache_path=".cache"))
user_id = sp.current_user().get("id")

year = user_date.split("-")[0]
all_uri = []

for song in all_songs:
    result = sp.search(q=f"track: {song}", type="track", limit=1)
    try:
        all_uri.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print("Song is not available on Spotify")

playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)
playlist_id = playlist["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=all_uri)
