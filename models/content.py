class Film:
    def __init__(
            self, name, description,
            genre, country, year, rating,
            director, duration, budget, url
    ):
        self.name = name
        self.description = description
        self.genre = genre
        self.country = country
        self.year = year
        self.rating = rating
        self.director = director
        self.duration = duration
        self.budget = budget
        self.url = url


class TvShow:
    def __init__(
            self, name, description,
            genre, country, year, rating,
            director, number_episodes, number_seasons, url
    ):
        self.name = name
        self.description = description
        self.genre = genre
        self.country = country
        self.year = year
        self.rating = rating
        self.director = director
        self.number_episodes = number_episodes
        self.number_seasons = number_seasons
        self.url = url


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
                                 tv_show_db['director'], tv_show_db['number_episodes'], tv_show_db['number_seasons'], tv_show_db['url']
                                 )
                list_tv_shows.append(tv_show)
        return list_tv_shows
