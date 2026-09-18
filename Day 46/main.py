import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

BASE_URL = "https://appbrewery.github.io/bakeboard-hot-100"

user_input = input(
    "Which year do you want to travel to? Type the date in the format YYYY-MM-DD: "
)

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

response = requests.get(f"{BASE_URL}/{user_input}", headers=header)
response.raise_for_status()

bakeboard_website = response.text
soup = BeautifulSoup(bakeboard_website, "html.parser")

songs = [song.getText().strip() for song in soup.select(".chart-entry__title")]
artists = [artist.getText().strip() for artist in soup.select(".chart-entry__artist")]

scope = "playlist-modify-private"

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

song_uris = []

for song, artist in zip(songs, artists):
    try:
        song_uris.append(
            sp.search(q=f"track:{song} artist:{artist}", type="track", limit=1)[
                "tracks"
            ]["items"][0]["uri"]
        )
    except IndexError:
        try:
            song_uris.append(
                sp.search(q=f"track:{song}", type="track", limit=1)["tracks"]["items"][
                    0
                ]["uri"]
            )
        except IndexError:
            print(f"Could not find: {song} by {artist}")

playlist_id = sp.current_user_playlist_create(
    name=f"{user_input} Billboard 100",
    public=False,
    collaborative=False,
    description="Testing",
)["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
