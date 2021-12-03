import pymysql
from config import host, userDb, passwordDb, db_name


class User:
    def __init__(self, login):
        self.login = login

    def _connect_db(self):
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=userDb,
            password=passwordDb,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection

    def get_rating_list_film(self):
        rating_list_films = []
        try:
            connection = self._connect_db()
            print("Good")
            try:
                with connection.cursor() as cursor:
                    select_all_rows = 'SELECT * FROM `rating_user_film` WHERE login = \'' + self.login + "\'"
                    cursor.execute(select_all_rows)
                    row = cursor.fetchall()
                    rating_list_films = row
            finally:
                connection.close()
        except Exception as ex:
            print("not good")
            print(ex)
        return rating_list_films

    def get_rating_list_tv_show(self):
        rating_list_tv_show = []
        try:
            connection = self._connect_db()
            print("Good")
            try:
                with connection.cursor() as cursor:
                    select_all_rows = 'SELECT * FROM `rating_user_tv_show` WHERE login = \'' + self.login + "\'"
                    cursor.execute(select_all_rows)
                    row = cursor.fetchall()
                    rating_list_tv_show = row
            finally:
                connection.close()
        except Exception as ex:
            print("not good")
            print(ex)
        return rating_list_tv_show


