"""Displays a page that shows my most favouritest movies"""

import fresh_tomatoes
import re

class Movie(object):
    """Contains information needed to present a movie"""

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = 'resources/posters/' + poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def youtube_id(self):
        """Pulls the YouTube ID out of a YouTube URL"""
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', self.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', self.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
        return trailer_youtube_id

    def srcset(self):
        """Creates an appropriate srcset for serving retina images"""
        file_extension_start = self.poster_image_url.find('.jpg')
        srcset_1x = self.poster_image_url + ' 1x'
        srcset_2x = self.poster_image_url[:file_extension_start] + '@2x.jpg 2x'
        return srcset_1x + ', ' + srcset_2x

movies = [
    Movie(
        'Life of Brian',
        'life-of-brian.jpg',
        'https://www.youtube.com/watch?v=tOOVm4kY4lE'
    ),
    Movie(
        'The Meaning of Life',
        'meaning-of-life.jpg',
        'https://www.youtube.com/watch?v=54ulXNk-bmo'
    ),
    Movie(
        'Monty Python and The Holy Grail',
        'holy-grail.jpg',
        'https://www.youtube.com/watch?v=LG1PlkURjxE'
    )
]

fresh_tomatoes.open_movies_page(movies)
