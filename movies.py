"""Displays a page that shows my most favouritest movies"""

import fresh_tomatoes

class Movie(object):
    """Contains information needed to present a movie"""

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

movies = [
    Movie(
        'Life of Brian',
        'http://ayay.co.uk/movies/poster/comedy/life-of-brian-re-release-2004.jpg',
        'https://www.youtube.com/watch?v=tOOVm4kY4lE'
    ),
    Movie(
        'The Meaning of Life',
        'http://cdn.collider.com/wp-content/uploads/monty-python-the-meaning-of-life-poster.jpg',
        'https://www.youtube.com/watch?v=54ulXNk-bmo'
    ),
    Movie(
        'The Holy Grail',
        'http://lsc.mit.edu/schedule/2014.2q/poster-montypythonandtheholygrail.jpg',
        'https://www.youtube.com/watch?v=LG1PlkURjxE'
    )
]

fresh_tomatoes.open_movies_page(movies)
