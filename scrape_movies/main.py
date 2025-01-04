from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/"
                        "https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text

soup = BeautifulSoup(data, "html.parser")
list_of_titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]
list_of_titles.reverse()
# print(list_of_titles)

# for title in list_of_titles:
#     try:
#         with open("movies.txt", mode='a', encoding="utf-8") as my_movies:
#             my_movies.write(title + '\n')
#     except FileNotFoundError:
#         with open("movies.txt", mode='w', encoding="utf-8") as my_movies:
#             my_movies.write(title + '\n')

with open("movies.txt", mode='w', encoding="utf-8") as my_movies:
    for title in list_of_titles:
        my_movies.write(f"{title}\n")
