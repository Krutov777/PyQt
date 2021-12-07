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
