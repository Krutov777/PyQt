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

    def edit_rating_film(self, name_film, user_rating):
        return self.data_base.edit_user_rating_film(self.login, name_film, user_rating)

    def edit_rating_tv_show(self, name_tv_show, user_rating):
        return self.data_base.edit_user_rating_tv_show(self.login, name_tv_show, user_rating)

    def remove_user_rating_film(self, name_film):
        return self.data_base.delete_user_rating_film(self.login, name_film)

    def remove_user_rating_tv_show(self, name_tv_show):
        return self.data_base.delete_user_rating_tv_show(self.login, name_tv_show)

    def average_rating_film(self, name_film):
        return self.data_base.average_rating_film(name_film)

    def average_rating_tv_show(self, name_tv_show):
        return self.data_base.average_rating_tv_show(name_tv_show)

    def number_user_rating_film(self, name_film):
        return self.data_base.number_user_rating_film(name_film)

    def number_user_rating_tv_show(self, name_tv_show):
        return self.data_base.number_user_rating_tv_show(name_tv_show)

    def get_user_rating_film(self, name_film):
        return self.data_base.get_user_rating_film(self.login, name_film)

    def get_user_rating_tv_show(self, name_tv):
        return self.data_base.get_user_rating_tv(self.login, name_tv)
