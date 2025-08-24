import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")
all_movies = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]

with open("top_movies.txt", mode="w") as file:
    for x in range(len(all_movies), 0, -1):
        file.write(f"{all_movies[x-1]}\n")
