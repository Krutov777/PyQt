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

    def get_user_rating_films(self):
        return self.user.get_user_rating_films()

    def get_user_rating_tv_shows(self):
        return self.get_user_rating_tv_shows()

    def edit_user_rating_film(self, name_film, user_rating):
        return self.user.edit_rating_film(name_film, user_rating)

    def edit_user_rating_tv_show(self, name_film, user_rating):
        return self.user.edit_rating_tv_show(name_film, user_rating)
