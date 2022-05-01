import requests
from bs4 import BeautifulSoup

AUTH_URL = ''
BASE_URL = ''
CLIENT_ID = ""
CLIENT_SECRET = ""
auth_response = requests.post(AUTH_URL, {"grant_type": "client_credentials",
                                         "client_id": CLIENT_ID,
                                         "client_secret": CLIENT_SECRET,
                                         }
                              )

auth_response_data = auth_response.json()
access_token = auth_response_data["access_token"]

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

DATE = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")


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


response = requests.get(f"https://www.billboard.com/charts/hot-100/{DATE}/")
song_title_page = response.text
soup = BeautifulSoup(song_title_page, "html.parser")
table = soup.find_all("div", class_="o-chart-results-list-row-container")
top100 = [get_deatails(item) for item in table]

print(top100)
