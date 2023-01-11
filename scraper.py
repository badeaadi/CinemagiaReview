import pandas as pd
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
        comment_title = review.find_all('h5', 'mb5')
        stars_symbol = review.find_all('span', 'stelutze')

        if len(stars_symbol) != 1 or len(comment_title) != 1:
            continue

        total_number_of_stars = stars_symbol[0].find_all('img')
        given_stars = 0
        for star in total_number_of_stars:
            if 'https://static.cinemagia.ro/img/star_full.gif' in star.attrs['src']:
                given_stars += 1

        paragraph = review.find_all('div', 'left comentariu')

        if len(total_number_of_stars):
            cnt += 1
            rating = str(given_stars / len(total_number_of_stars))
            title_with_comment = comment_title[0].text + '.' + (
                paragraph[0].text.replace('\n', ' ').strip(' ').strip("\""))
            data.append((movie_title, rating, title_with_comment))
    return cnt


data = []
movies_list = [
    (
        "Lord of the rings", 5,
        "https://www.cinemagia.ro/filme/the-lord-of-the-rings-the-fellowship-of-the-ring-stapanul-inelelor-fratia-2360/reviews/"),
    (
        "The Shawshank Redemption", 7,
        "https://www.cinemagia.ro/filme/the-shawshank-redemption-inchisoarea-ingerilor-2304/reviews/"
    ),
    (
        "Game of Thrones", 4,
        "https://www.cinemagia.ro/filme/game-of-thrones-566508/reviews/"
    ),
    (
        "Prison Break", 5,
        "https://www.cinemagia.ro/filme/prison-break-19951/reviews/"
    ),
    (
        "Avatar", 12,  # 15 max
        "https://www.cinemagia.ro/filme/avatar-17818/reviews/"
    ),
    (
        "Schindler's List", 5,
        "https://www.cinemagia.ro/filme/schindlers-list-lista-lui-schindler-1085/reviews/"
    ),
    (
        "Harry Potter and the Goblet of Fire", 8,
        "https://www.cinemagia.ro/filme/harry-potter-and-the-goblet-of-fire-harry-potter-si-pocalul-de-foc-4885/reviews/"
    ),
    (
        "Pirates of the Caribbean: The Curse of the Black Pearl", 5,
        "https://www.cinemagia.ro/filme/pirates-of-the-caribbean-the-curse-of-the-black-pearl-4532/reviews/"
    ),
    (
        "Gone with the wind", 3,
        "https://www.cinemagia.ro/filme/gone-with-the-wind-pe-aripile-vantului-3883/reviews/"
    ),
    (
        "Hachiko: A Dog's Story", 8,
        "https://www.cinemagia.ro/filme/hachiko-a-dogs-story-hachi-44561/reviews/"
    )
]

for movie in movies_list:
    total = 0
    for index in range(1, movie[1] + 1):
        total += scrape(movie[0], movie[2] + "?pagina=" + str(index))
    print(str(total) + ' - ' + movie[0])

df = pd.DataFrame(data, columns=['Title', "Rating", 'Comment'])
df.to_csv('reviews.csv', sep=',', encoding='utf-8', index=False)
