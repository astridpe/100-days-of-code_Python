import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_REDIRECT_URI = ""
CLIENT_ID = ""
CLIENT_SECRET = ""

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]


def get_deatails(bill_board_entry):
    # Rank:
    meta_data = bill_board_entry.select("li, span")
    rank = meta_data[0].getText().strip("\t\n\t\n\n\n\t\n\tNEW")

    # Title:
    heading = bill_board_entry.find("h3")
    title = heading.getText().strip("\t\n\t")

    # Artist:
    artist = heading.find_next_sibling("span").getText().strip("\t\n\t")

    return rank, title, artist


DATE = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{DATE}/")
song_title_page = response.text
soup = BeautifulSoup(song_title_page, "html.parser")
table = soup.find_all("div", class_="o-chart-results-list-row-container")
top100 = [get_deatails(item) for item in table]

title_names = [title[1] for title in top100]
song_uris = []
year = DATE.split("-")[0]
playlist = sp.user_playlist_create(user=user_id, name=f"{DATE} - Billboard 100", public=False)

for title in title_names:
    result = sp.search(q=f"track:{title} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)

    except IndexError:
        print(f"'{title}' doesn't exist in Spotify. Skipped.")

sp.playlist_add_items(playlist["id"], song_uris)

