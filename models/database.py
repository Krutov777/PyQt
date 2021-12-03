import pymysql
from config import host, userDb, passwordDb, db_name


class DataBase:
    def __init__(self):
        pass

    @staticmethod
    def _connect_db():
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
                    select_id_user = 'SELECT id_user FROM `user` WHERE login = \'' + login + "\'"
                    cursor.execute(select_id_user)
                    id_user = cursor.fetchall()
                    select_all_rows = 'SELECT * FROM `rating_user_film` WHERE id_user = \'' \
                                      + str(id_user[0]['id_user']) + "\'"
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
                    select_id_user = 'SELECT id_user FROM `user` WHERE login = \'' + login + "\'"
                    cursor.execute(select_id_user)
                    id_user = cursor.fetchall()
                    select_all_rows = 'SELECT * FROM `rating_user_tv_show` WHERE id_user = \'' \
                                      + str(id_user[0]['id_user']) + "\'"
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

    def edit_user_rating_film(self, username, name_film, user_rating):
        try:
            connection = self._connect_db()
            try:
                with connection.cursor() as cursor:
                    select_id_user = 'SELECT id_user FROM `user` WHERE login = \'' + username + "\'"
                    cursor.execute(select_id_user)
                    id_user = cursor.fetchall()
                    select_id_film = 'SELECT id_film FROM `film` WHERE name_film = \'' + name_film + "\'"
                    cursor.execute(select_id_film)
                    id_film = cursor.fetchall()
                    select_user_rating = 'SELECT id FROM `rating_user_film` WHERE id_user = \'' \
                                         + str(id_user[0]['id_user']) + "\'" \
                                                                        " AND id_film = \'" \
                                         + str(id_film[0]['id_film']) + "\'"
                    cursor.execute(select_user_rating)
                    id_user_rating = cursor.fetchall()
                    if len(id_user_rating) > 0:
                        query = 'UPDATE `rating_user_film` SET rating_user = \'' \
                                + str(user_rating) + "\'" \
                                                     " WHERE id = \'" \
                                + str(id_user_rating[0]['id']) + "\'"
                        cursor.execute(query)
                        connection.commit()
                    else:
                        query = 'INSERT INTO `rating_user_film` (id_film, id_user, rating_user) VALUES (%s, %s, %s)'
                        val = (int(id_film[0]['id_film']), int(id_user[0]['id_user']), int(user_rating))
                        cursor.execute(query, val)
                        connection.commit()
            finally:
                connection.close()
        except Exception as ex:
            print(ex)

    def edit_user_rating_tv_show(self, username, name_tv_show, user_rating):
        try:
            connection = self._connect_db()
            try:
                with connection.cursor() as cursor:
                    select_id_user = 'SELECT id_user FROM `user` WHERE login = \'' + username + "\'"
                    cursor.execute(select_id_user)
                    id_user = cursor.fetchall()
                    select_id_tv_show = 'SELECT id_tv_show FROM `film` WHERE name_tv_show = \'' + name_tv_show + "\'"
                    cursor.execute(select_id_tv_show)
                    id_tv_show = cursor.fetchall()
                    select_user_rating = 'SELECT id FROM `rating_user_tv_show` WHERE id_user = \'' \
                                         + str(id_user[0]['id_user']) + "\'" \
                                                                        " AND id_tv_show = \'" \
                                         + str(id_tv_show[0]['id_tv_show']) + "\'"
                    cursor.execute(select_user_rating)
                    id_user_rating = cursor.fetchall()
                    if len(id_user_rating) > 0:
                        query = 'UPDATE `rating_user_tv_show` SET rating_user = \'' \
                                + str(user_rating) + "\'" \
                                                     " WHERE id = \'" \
                                + str(id_user_rating[0]['id']) + "\'"
                        cursor.execute(query)
                        connection.commit()
                    else:
                        query = 'INSERT INTO `rating_user_tv_show` (id_tv_show, id_user, rating_user)' \
                                ' VALUES (%s, %s, %s)'
                        val = (int(id_tv_show[0]['id_tv_show']), int(id_user[0]['id_user']), int(user_rating))
                        cursor.execute(query, val)
                        connection.commit()
            finally:
                connection.close()
        except Exception as ex:
            print(ex)

    def delete_user_rating_film(self, username, name_film):
        try:
            connection = self._connect_db()
            try:
                with connection.cursor() as cursor:
                    select_id_user = 'SELECT id_user FROM `user` WHERE login = \'' + username + "\'"
                    cursor.execute(select_id_user)
                    id_user = cursor.fetchall()
                    select_id_film = 'SELECT id_film FROM `film` WHERE name_film = \'' + name_film + "\'"
                    cursor.execute(select_id_film)
                    id_film = cursor.fetchall()
                    select_user_rating = 'SELECT id FROM `rating_user_film` WHERE id_user = \'' \
                                         + str(id_user[0]['id_user']) + "\'" \
                                                                        " AND id_film = \'" \
                                         + str(id_film[0]['id_film']) + "\'"
                    cursor.execute(select_user_rating)
                    id_user_rating = cursor.fetchall()
                    if len(id_user_rating) > 0:
                        query = 'DELETE FROM `rating_user_film` WHERE id_user = \'' \
                                + str(id_user[0]['id_user']) + "\' " \
                                                               " AND id_film = \'" \
                                + str(id_film[0]['id_film']) + "\'"
                        cursor.execute(query)
                        connection.commit()
            finally:
                connection.close()
        except Exception as ex:
            print(ex)

    def delete_user_rating_tv_show(self, username, name_tv_show):
        try:
            connection = self._connect_db()
            try:
                with connection.cursor() as cursor:
                    select_id_user = 'SELECT id_user FROM `user` WHERE login = \'' + username + "\'"
                    cursor.execute(select_id_user)
                    id_user = cursor.fetchall()
                    select_id_tv_show = 'SELECT id_tv_show FROM `film` WHERE name_tv_show = \'' + name_tv_show + "\'"
                    cursor.execute(select_id_tv_show)
                    id_tv_show = cursor.fetchall()
                    select_user_rating = 'SELECT id FROM `rating_user_tv_show` WHERE id_user = \'' \
                                         + str(id_user[0]['id_user']) + "\'" \
                                                                        " AND id_tv_show = \'" \
                                         + str(id_tv_show[0]['id_tv_show']) + "\'"
                    cursor.execute(select_user_rating)
                    id_user_rating = cursor.fetchall()
                    if len(id_user_rating) > 0:
                        query = 'DELETE FROM `rating_user_tv_show` WHERE id_user = \'' \
                                + str(id_user[0]['id_user']) + "\' " \
                                                               " AND id_tv_show = \'" \
                                + str(id_tv_show[0]['id_tv_show']) + "\'"
                        cursor.execute(query)
                        connection.commit()
            finally:
                connection.close()
        except Exception as ex:
            print(ex)

    def average_rating_film(self, name_film):
        average_rating_film = "Нет оценок"
        try:
            connection = self._connect_db()
            try:
                with connection.cursor() as cursor:

                    select_id_film = 'SELECT id_film FROM `film` WHERE name_film = \'' + name_film + "\'"
                    cursor.execute(select_id_film)
                    id_film = cursor.fetchall()
                    select_rating_film = 'SELECT rating_user FROM `rating_user_film` WHERE id_film = \'' + str(id_film[0]['id_film']) + "\'"
                    cursor.execute(select_rating_film)
                    list_rating_film = cursor.fetchall()
                    divider = len(list_rating_film)
                    dividend = 0
                    if divider > 0:
                        for rating_film in list_rating_film:
                            dividend = dividend + int(rating_film['rating_user'])
                        average_rating_film = f"{dividend/divider:.{2}f}"
            finally:
                connection.close()
        except Exception as ex:
            print(ex)
        return average_rating_film

    def average_rating_tv_show(self, name_tv_show):
        average_rating_tv_show = "Нет оценок"
        try:
            connection = self._connect_db()
            try:
                with connection.cursor() as cursor:
                    select_id_tv_show = 'SELECT id_tv_show FROM `tv_show` WHERE name_tv_show = \'' + name_tv_show + "\'"
                    cursor.execute(select_id_tv_show)
                    id_tv_show = cursor.fetchall()
                    select_rating_tv_show = 'SELECT rating_user FROM `rating_user_tv_show` ' \
                                            'WHERE id_tv_show = \''\
                                            + str(id_tv_show[0]['id_tv_show']) + "\'"
                    cursor.execute(select_rating_tv_show)
                    list_rating_tv_show = cursor.fetchall()
                    divider = len(list_rating_tv_show)
                    dividend = 0
                    if divider > 0:
                        for rating in list_rating_tv_show:
                            dividend = dividend + int(rating['rating_user'])
                        average_rating_tv_show = f"{dividend/divider:.{2}f}"
            finally:
                connection.close()
        except Exception as ex:
            print(ex)
        return average_rating_tv_show
