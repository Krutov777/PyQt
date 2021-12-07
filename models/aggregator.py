import requests
from PyQt5.QtGui import QImage, QIcon, QPixmap

from models.content import ContentList
from models.user import User


class Aggregator:
    def __init__(self):
        self.user = User('')

    def get_content_list(self):
        return ContentList(self.user.get_list_films(), self.user.get_list_tv_show())

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
