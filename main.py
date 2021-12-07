import sys

import requests as requests
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import QDialog, QApplication, QListWidget, QListWidgetItem
from PyQt5.uic import loadUi
from models.aggregator import *


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("UI/welcomescreen.ui", self)
        self.login.clicked.connect(self.gotoLogin)
        self.create.clicked.connect(self.gotoCreate)

    @staticmethod
    def gotoLogin():
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    @staticmethod
    def gotoCreate():
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("UI/login.ui", self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginFunction)
        self.back.clicked.connect(self.goto_welcome_screen)

    def loginFunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()

        if len(user) == 0 or len(password) == 0:
            self.error.setText("Please input all fields.")

        else:
            if aggregator.login(user, password):
                self.gotoChoiceOfAction()
                print("Successfully logged in.")
                self.error.setText("")
            else:
                self.error.setText("Invalid username or password")

    def gotoChoiceOfAction(self):
        choiceOfAction = ChoiceOfAction()
        self.login.clicked.connect(self.gotoChoiceOfAction)
        widget.addWidget(choiceOfAction)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    @staticmethod
    def goto_welcome_screen():
        aggregator.user.set_login('')
        welcome_screen = WelcomeScreen()
        widget.addWidget(welcome_screen)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ChoiceOfAction(QDialog):
    def __init__(self):
        super(ChoiceOfAction, self).__init__()
        loadUi("UI/choiceofaction.ui", self)
        self.listFilms.clicked.connect(self.display_list_films)
        self.listTv.clicked.connect(self.display_list_tv)
        self.logout.clicked.connect(self.goto_welcome_screen)

    def display_list_films(self):
        list_films = ListFilms()
        self.listFilms.clicked.connect(self.display_list_films)
        widget.addWidget(list_films)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def display_list_tv(self):
        list_tv = ListTv()
        self.listTv.clicked.connect(self.display_list_tv)
        widget.addWidget(list_tv)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    @staticmethod
    def goto_welcome_screen():
        aggregator.user.set_login('')
        welcome_screen = WelcomeScreen()
        widget.addWidget(welcome_screen)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ListFilms(QDialog, QListWidget):
    def __init__(self):
        super(ListFilms, self).__init__()
        self.resize(1200, 800)
        self.setStyleSheet('font-size: 40px')
        loadUi("UI/films.ui", self)
        content_list = aggregator.get_content_list()
        list_films = content_list.list_films
        self.listFilms.setViewMode(QListWidget.IconMode)
        self.listFilms.setResizeMode(QListWidget.Adjust)
        self.listFilms.setSpacing(10)
        icon_size = QSize()
        icon_size.setHeight(150)
        icon_size.setWidth(150)
        self.listFilms.setIconSize(icon_size)
        self.listFilms.setMovement(QListWidget.Static)
        for film in list_films:
            item = QListWidgetItem(film.name)
            item.setIcon(QIcon(aggregator.parse_image(film.url)))
            item.setSizeHint(QSize(200, 200))
            self.listFilms.addItem(item)

        self.addRating.clicked.connect(self.add_sel_rating)
        self.removeRating.clicked.connect(self.del_sel_rating)
        self.listFilms.itemDoubleClicked.connect(self.launch_more_info)
        self.back.clicked.connect(self.goto_choice_of_action)

    @staticmethod
    def goto_choice_of_action():
        choice_of_action = ChoiceOfAction()
        widget.addWidget(choice_of_action)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def add_sel_rating(self):
        rating = self.spinRating.text()
        film = self.listFilms.selectedItems()
        if len(film) > 0:
            film = film[0]
            aggregator.edit_user_rating_film(film.text(), rating)

    def del_sel_rating(self):
        film = self.listFilms.selectedItems()
        if len(film) > 0:
            film = film[0]
            aggregator.remove_user_rating_film(film.text())

    def launch_more_info(self, item):
        content_list = aggregator.get_content_list()
        list_films = content_list.list_films
        for film in list_films:
            if film.name == item.text():
                pop = MoreInfoForFilm(film, self)
                pop.show()


class MoreInfoForFilm(QDialog):
    def __init__(self, film, parent):
        super().__init__(parent)
        loadUi("UI/moreInfoForFilm.ui", self)
        self.name_film.setText(film.name)
        self.year.setText(str(film.year))
        self.country.setText(film.country)
        self.director.setText(film.director)
        self.duration.setText(str(film.duration) + ' min')
        self.genre.setText(film.genre)
        self.budget.setText(str(film.budget) + ' $$$')
        self.rating.setText(str(film.rating))
        self.description.setText(film.description)
        self.average_rating.setText(str(aggregator.average_rating_film(film.name)))
        self.number_rating.setText(str(aggregator.number_user_rating_film(film.name)))
        self.my_rating.setText(str(aggregator.get_user_rating_film(film.name)))

        image = QPixmap(aggregator.parse_image(film.url))
        self.image.setPixmap(image.scaledToWidth(312))

        self.add_rating.clicked.connect(self.add_rating_film)
        self.remove_rating.clicked.connect(self.del_rating_film)

    def add_rating_film(self):
        rating = self.spinRating.text()
        if len(rating) > 0:
            aggregator.edit_user_rating_film(self.name_film.text(), rating)
            self.average_rating.setText(str(aggregator.average_rating_film(self.name_film.text())))
            self.number_rating.setText(str(aggregator.number_user_rating_film(self.name_film.text())))
            self.my_rating.setText(str(aggregator.get_user_rating_film(self.name_film.text())))

    def del_rating_film(self):
        aggregator.remove_user_rating_film(self.name_film.text())
        self.average_rating.setText(str(aggregator.average_rating_film(self.name_film.text())))
        self.number_rating.setText(str(aggregator.number_user_rating_film(self.name_film.text())))
        self.my_rating.setText(str(aggregator.get_user_rating_film(self.name_film.text())))


class ListTv(QDialog, QListWidget):
    def __init__(self):
        super(ListTv, self).__init__()
        self.resize(1200, 800)
        self.setStyleSheet('font-size: 40px')
        loadUi("UI/tv.ui", self)
        content_list = aggregator.get_content_list()
        list_tv = content_list.list_tv_shows
        self.listTv.setViewMode(QListWidget.IconMode)
        self.listTv.setResizeMode(QListWidget.Adjust)
        self.listTv.setSpacing(10)
        icon_size = QSize()
        icon_size.setHeight(150)
        icon_size.setWidth(150)
        self.listTv.setIconSize(icon_size)
        self.listTv.setMovement(QListWidget.Static)
        for tv in list_tv:
            item = QListWidgetItem(tv.name)
            item.setIcon(QIcon(aggregator.parse_image(tv.url)))
            item.setSizeHint(QSize(200, 200))
            self.listTv.addItem(item)

        self.addRating.clicked.connect(self.add_sel_rating)
        self.removeRating.clicked.connect(self.del_sel_rating)
        self.listTv.itemDoubleClicked.connect(self.launch_more_info)
        self.back.clicked.connect(self.goto_choice_of_action)

    @staticmethod
    def goto_choice_of_action():
        choice_of_action = ChoiceOfAction()
        widget.addWidget(choice_of_action)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def add_sel_rating(self):
        rating = self.spinRating.text()
        tv = self.listTv.selectedItems()
        if len(tv) > 0:
            tv = tv[0]
            aggregator.edit_user_rating_tv_show(tv.text(), rating)

    def del_sel_rating(self):
        tv = self.listTv.selectedItems()
        if len(tv) > 0:
            tv = tv[0]
            aggregator.remove_user_rating_tv_show(tv.text())

    def launch_more_info(self, item):
        content_list = aggregator.get_content_list()
        list_tv = content_list.list_tv_shows
        for tv in list_tv:
            if tv.name == item.text():
                pop = MoreInfoForTv(tv, self)
                pop.show()


class MoreInfoForTv(QDialog):
    def __init__(self, tv, parent):
        super().__init__(parent)
        loadUi("UI/moreInfoForTv.ui", self)
        self.name_tv.setText(tv.name)
        self.year.setText(str(tv.year))
        self.country.setText(tv.country)
        self.director.setText(tv.director)
        self.number_seasons.setText(str(tv.number_seasons))
        self.genre.setText(tv.genre)
        self.number_episodes.setText(str(tv.number_episodes))
        self.rating.setText(str(tv.rating))
        self.description.setText(tv.description)
        self.average_rating.setText(str(aggregator.average_rating_tv_show(tv.name)))
        self.number_rating.setText(str(aggregator.number_user_rating_tv_show(tv.name)))
        self.my_rating.setText(str(aggregator.get_user_rating_tv(tv.name)))

        image = QPixmap(aggregator.parse_image(tv.url))
        self.image.setPixmap(image.scaledToWidth(312))

        self.add_rating.clicked.connect(self.add_rating_tv)
        self.remove_rating.clicked.connect(self.del_rating_tv)

    def add_rating_tv(self):
        rating = self.spinRating.text()
        if len(rating) > 0:
            aggregator.edit_user_rating_tv_show(self.name_tv.text(), rating)
            self.average_rating.setText(str(aggregator.average_rating_tv_show(self.name_tv.text())))
            self.number_rating.setText(str(aggregator.number_user_rating_tv_show(self.name_tv.text())))
            self.my_rating.setText(str(aggregator.get_user_rating_tv(self.name_tv.text())))

    def del_rating_tv(self):
        aggregator.remove_user_rating_tv_show(self.name_tv.text())
        self.average_rating.setText(str(aggregator.average_rating_tv_show(self.name_tv.text())))
        self.number_rating.setText(str(aggregator.number_user_rating_tv_show(self.name_tv.text())))
        self.my_rating.setText(str(aggregator.get_user_rating_tv(self.name_tv.text())))


class CreateAccScreen(QDialog):
    def __init__(self):
        super(CreateAccScreen, self).__init__()
        loadUi("UI/createacc.ui", self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.signupFunction)
        self.back.clicked.connect(self.goto_welcome_screen)

    def signupFunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()
        confirmPassword = self.confirmpasswordfield.text()

        if len(user) == 0 or len(password) == 0 or len(confirmPassword) == 0:
            self.error.setText("Please fill in all inputs.")

        elif password != confirmPassword:
            self.error.setText("Passwords do not match.")

        else:
            if aggregator.signup(user, password):
                self.gotoLogin()
                print("Successfully signup in.")

            else:
                self.error.setText("User with this name is already registered")

    def gotoLogin(self):
        login = LoginScreen()
        self.signup.clicked.connect(self.gotoLogin)
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    @staticmethod
    def goto_welcome_screen():
        aggregator.user.set_login('')
        welcome_screen = WelcomeScreen()
        widget.addWidget(welcome_screen)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# main
aggregator = Aggregator()
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
