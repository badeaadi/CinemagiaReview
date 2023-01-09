import csv

import requests
from bs4 import BeautifulSoup


def scrape(movie_title, url):
    # Make a request to the webpage
    r = requests.get(url)

    # Extract the HTML from the request
    html = r.text

    # Create a BeautifulSoup object from the HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Find all the <p> elements on the page
    reviews = soup.find_all('div', 'post clearfix')
    cnt = 0
    for review in reviews:
        title = review.find_all('h5', 'mb5')
        stars_symbol = review.find_all('span', 'stelutze')

        if len(stars_symbol) != 1 or len(title) != 1:
            continue

        stars = stars_symbol[0].find_all('img')
        paragraph = review.find_all('div', 'left comentariu')

        if len(stars):
            cnt += 1
            f.write(title[0].text + '\n')
            f.write(str(len(stars)) + '\n')
            f.write((paragraph[0].text.replace('\n', ' ').strip(' ').strip("\"")) + '\n\n')
    print(cnt)

f = open('reviews.csv', 'w', encoding="utf-8")
scrape(
    "Lord of the rings", 'https://www.cinemagia.ro/filme/the-lord-of-the-rings-the-fellowship-of-the-ring-stapanul-inelelor-fratia-2360/reviews/')

f.close()
