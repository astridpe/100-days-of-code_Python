import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movie_web_page = response.text
soup = BeautifulSoup(movie_web_page, "html.parser")
movie_titles = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")






