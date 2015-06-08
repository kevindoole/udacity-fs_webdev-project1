"""Provides data about my most favouritest movies"""

class Movie(object):
    """Contains information needed to present a movie"""

    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        self.movie_title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
