import requests
from bs4 import BeautifulSoup
# import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date_str = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date_str}/"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=URL, headers=header)
# print(response)
webpage = response.text
# print(webpage)

soup = BeautifulSoup(webpage, "html.parser")

artist_response_list = soup.select(selector="li.lrv-u-width-100p li.o-chart-results-list__item span.c-label")

list_of_titles = [title.getText().strip() for title in soup.select(selector="li h3.c-title")]
list_of_artists = [item.getText().split("&")[0].strip() for
                   item in artist_response_list if (artist_response_list.index(item) % 7 == 0)]
print(list_of_titles, len(list_of_titles))
print(list_of_artists, len(list_of_artists))

CLIENT_ID = "285e9fcbb6144df0a2c00e1d7381e921"
CLIENT_SECRET = "5671e98913c44187a4a1ed3023ae0e39"
REDIRECT_URI = "http://example.com"
# GET_URL = "https://accounts.spotify.com/authorize"
# POST_URL = "https://api.spotify.com/v1"
scope = "playlist-modify-private"

with open("./.cache") as file:
    data = file.read()
    token = data.split('"')[3]  # not required
    # print(token)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope))
user = sp.current_user()
# print(user["id"])
USER_ID = "31fmutykzxlfooigh5y2c7tvl3hm"

play_list = sp.user_playlist_create(user=USER_ID, name=f"{date_str} Billboard 100", public=False)
# print(play_list)

list_of_song_uris = []
for song_name in list_of_titles:
    query = f"{song_name} {list_of_artists[list_of_titles.index(song_name)].split()[0]}"
    response = sp.search(q=query)
    song_uri = response["tracks"]["items"][0]["uri"]
    # print(song_uri)
    try:
        list_of_song_uris.append(song_uri)
    except IndexError:
        continue

print(len(list_of_song_uris))
sp.playlist_add_items(playlist_id=play_list["id"], items=list_of_song_uris)
