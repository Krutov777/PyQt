import pymysql
from config import host, userDb, passwordDb, db_name


class DataBase:
    def __init__(self):
        pass

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

    def get_user_rating_list_film(self, login):
        rating_list_films = []
        try:
            connection = self._connect_db()
            try:
                with connection.cursor() as cursor:
                    select_all_rows = 'SELECT * FROM `rating_user_film` WHERE login = \'' + login + "\'"
                    cursor.execute(select_all_rows)
                    row = cursor.fetchall()
                    rating_list_films = row
            finally:
                connection.close()
        except Exception as ex:
            print(ex)
        return rating_list_films

    def get_user_rating_list_tv_show(self, login):
        rating_list_tv_show = []
        try:
            connection = self._connect_db()
            try:
                with connection.cursor() as cursor:
                    select_all_rows = 'SELECT * FROM `rating_user_tv_show` WHERE login = \'' + login + "\'"
                    cursor.execute(select_all_rows)
                    row = cursor.fetchall()
                    rating_list_tv_show = row
            finally:
                connection.close()
        except Exception as ex:
            print(ex)
        return rating_list_tv_show

    def login(self, username, password):
        isLogin = False
        try:
            connection = self._connect_db()
            try:
                with connection.cursor() as cursor:
                    query = 'SELECT password FROM `user` WHERE login = \'' + username + "\'"
                    cursor.execute(query)
                    row = cursor.fetchall()
                    if row[0]['password'] == password:
                        isLogin = True
            finally:
                connection.close()
        except Exception as ex:
            print(ex)
        return isLogin

    def get_list_films_from_db(self):
        films = []
        try:
            connection = self._connect_db()
            try:
                with connection.cursor() as cursor:
                    select_all_rows = "SELECT * FROM `film`"
                    cursor.execute(select_all_rows)
                    row = cursor.fetchall()
                    films = [film for film in row]
                    return films
            finally:
                connection.close()
        except Exception as ex:
            print(ex)
        return films

    def get_list_tv_show_from_db(self):
        tv_shows = []
        try:
            connection = self._connect_db()
            try:
                with connection.cursor() as cursor:
                    select_all_rows = "SELECT * FROM `tv_show`"
                    cursor.execute(select_all_rows)
                    row = cursor.fetchall()
                    tv_shows = [tv_show for tv_show in row]
                    return tv_shows
            finally:
                connection.close()
        except Exception as ex:
            print(ex)
        return tv_shows

    def signup(self, username, password):
        signup = False
        try:
            connection = self._connect_db()
            try:
                with connection.cursor() as cursor:
                    query = 'SELECT password FROM `user` WHERE login = \'' + username + "\'"
                    cursor.execute(query)
                    row = cursor.fetchall()
                    if len(row) == 0:
                        with connection.cursor() as cur:
                            query = 'INSERT INTO `user` (login, password) VALUES (%s, %s)'
                            val = (username, password)
                            cur.execute(query, val)
                            connection.commit()
                            return True
            finally:
                connection.close()
        except Exception as ex:
            print(ex)
        return signup
