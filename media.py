import webbrowser


class Movie(object):
    """Movie Class encapsulates movie information

     Attributes:
         movie_title: movie title string
         movie_storyline: movie story line string
         poster_image: URL to movie poster image JPG
         trailer_youtube: URL to movie trailer youtube page
     """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """Inits Movie class with its attributes"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Launch webbrowser and open movie trailer youtube URL trailer_youtube"""
        webbrowser.open(self.trailer_youtube_url)
