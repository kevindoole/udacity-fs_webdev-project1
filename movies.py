"""Displays a page that shows my most favouritest movies"""

import fresh_tomatoes

class Movie(object):
    """Contains information needed to present a movie"""

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
