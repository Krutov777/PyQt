from models.database import DataBase


class User:
    def __init__(self, login):
        self.login = login
        self.data_base = DataBase()

    def get_user_rating_films(self):
        return self.data_base.get_user_rating_list_film(self.login)

    def get_user_rating_tv_shows(self):
        return self.data_base.get_user_rating_list_tv_show(self.login)

    def is_login(self, username, password):
        return self.data_base.login(username, password)

    def signup(self, username, password):
        return self.data_base.signup(username, password)

    def set_login(self, login):
        self.login = login

    def get_list_films(self):
        return self.data_base.get_list_films_from_db()

    def get_list_tv_show(self):
        return self.data_base.get_list_tv_show_from_db()


