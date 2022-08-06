import os.path
# import Beautiful soup
from bs4 import BeautifulSoup
# import requests
from requests import *

movie_url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
data = get(url=movie_url).text  # convert requests to text
# create a soup object
soup = BeautifulSoup(data, 'html.parser')
movies = [movie.getText() for movie in soup.find_all(name='h3', class_='title')]

# checking if movies.txt exists just incase this programe is ran more than once ... if it exists then it would clear it
if os.path.exists('movies.txt'):
    with open('movies.txt', 'w') as clean:
        clean.write('')
# the loop starts from the last item in the list to the first item in the list
for index in range(len(movies) - 1, -1, -1):
    with open('movies.txt', 'a') as title:
        movie_name = movies[index]
        title.write(f'{movie_name}\n')
