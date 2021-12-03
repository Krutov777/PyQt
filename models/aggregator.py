from models.content import ContentList
import pymysql
from models.user import User


class Aggregator:
    def __init__(self, host, user_db, password, db_name):
        self.host = host
        self.user_db = user_db
        self.user = None
        self.password = password
        self.db_name = db_name

        #self.contentList = ContentList(self._getListFilmsFromDb(), self._getListTvShowsFromDb())

    def get_content_list(self):
        return ContentList(self._get_list_films_from_db(), self._get_list_tv_show_from_db())

    def _connect_db(self):
        connection = pymysql.connect(
                host=self.host,
                port=3306,
                user=self.user_db,
                password=self.password,
                database=self.db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
        return connection

    def _get_list_films_from_db(self):
        films = []
        try:
            connection = self._connect_db()
            try:
                with connection.cursor() as cursor:
                    select_all_rows = "SELECT * FROM `film`"
                    cursor.execute(select_all_rows)
                    row = cursor.fetchall()
                    films = row
                    return films
            finally:
                connection.close()
        except Exception as ex:
            print(ex)
        return films

    def _get_list_tv_show_from_db(self):
        tv_shows = []
        try:
            connection = self._connect_db()
            try:
                with connection.cursor() as cursor:
                    select_all_rows = "SELECT * FROM `tv_show`"
                    cursor.execute(select_all_rows)
                    row = cursor.fetchall()
                    tv_shows = row
                    return tv_shows
            finally:
                connection.close()
        except Exception as ex:
            print(ex)
        return tv_shows

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
                        self.user = User(username)

            finally:
                connection.close()
        except Exception as ex:
            print(ex)
        return isLogin

    def signup(self, username, password):
        signup = False
        try:
            connection = self._connectMySQL()
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
