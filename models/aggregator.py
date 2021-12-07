import requests
from PyQt5.QtGui import QImage, QPixmap
from models.content import *
from models.user import User


class Aggregator:
    class ContentList:
        def __init__(self, list_films_db=None, list_tv_shows_db=None):
            if list_tv_shows_db is None:
                list_tv_shows_db = []
            if list_films_db is None:
                list_films_db = []
            self.list_films_db = list_films_db
            self.list_tv_shows_db = list_tv_shows_db
            self.list_films = self._get_list_films()
            self.list_tv_shows = self._get_list_tv_shows()

        def _get_list_films(self):
            list_films = []
            if len(self.list_films_db) > 0:
                for film_db in self.list_films_db:
                    """агрегация Film"""
                    film = Film(film_db['name_film'], film_db['description_film'], film_db['genre'],
                                film_db['country'], film_db['year_film'], film_db['rating'],
                                film_db['director'], film_db['duration'], film_db['budget'], film_db['url']
                                )
                    list_films.append(film)
            return list_films

        def _get_list_tv_shows(self):
            list_tv_shows = []
            if len(self.list_tv_shows_db) > 0:
                for tv_show_db in self.list_tv_shows_db:
                    """агрегация TvShow"""
                    tv_show = TvShow(tv_show_db['name_tv_show'], tv_show_db['description_tv_show'], tv_show_db['genre'],
                                     tv_show_db['country'], tv_show_db['year_tv_show'], tv_show_db['rating'],
                                     tv_show_db['director'], tv_show_db['number_episodes'],
                                     tv_show_db['number_seasons'], tv_show_db['url']
                                     )
                    list_tv_shows.append(tv_show)
            return list_tv_shows

    def __init__(self):
        self.user = User('')

    def get_content_list(self):
        return Aggregator.ContentList(self.user.get_list_films(), self.user.get_list_tv_show())

    def login(self, username, password):
        isLogin = self.user.is_login(username, password)
        if isLogin:
            self.user.set_login(username)
            return True
        else:
            return False

    def signup(self, username, password):
        return self.user.signup(username, password)

    def get_user_rating_film(self, name_film):
        return str(self.user.get_user_rating_film(name_film))

    def get_user_rating_tv(self, name_tv):
        return str(self.user.get_user_rating_tv_show(name_tv))

    def get_user_rating_films(self):
        return self.user.get_user_rating_films()

    def get_user_rating_tv_shows(self):
        return self.get_user_rating_tv_shows()

    def edit_user_rating_film(self, name_film, user_rating):
        return self.user.edit_rating_film(name_film, user_rating)

    def edit_user_rating_tv_show(self, name_film, user_rating):
        return self.user.edit_rating_tv_show(name_film, user_rating)

    def remove_user_rating_film(self, name_film):
        return self.user.remove_user_rating_film(name_film)

    def remove_user_rating_tv_show(self, name_tv_show):
        return self.user.remove_user_rating_tv_show(name_tv_show)

    def average_rating_film(self, name_film):
        return self.user.average_rating_film(name_film)

    def average_rating_tv_show(self, name_tv_show):
        return self.user.average_rating_tv_show(name_tv_show)

    def number_user_rating_film(self, name_film):
        return self.user.number_user_rating_film(name_film)

    def number_user_rating_tv_show(self, name_tv_show):
        return self.user.number_user_rating_tv_show(name_tv_show)

    @staticmethod
    def parse_image(url):
        image = QImage()
        if len(url) > 0:
            r = requests.get(url, stream=True)
            if r.status_code == 200:
                image.loadFromData(r.content)
                icon = QPixmap(image)
                return icon
        else:
            icon = QPixmap('/Users/i.krutov/PycharmProjects/pythonProjects/pyqt/images/not_found.jpg')
            return icon
