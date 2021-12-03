import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QListWidget, QLabel, QTabWidget, QWidget, QVBoxLayout
from PyQt5.uic import loadUi
from config import *
from models.aggregator import *
from models.content import *


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("UI/welcomescreen.ui", self)
        self.login.clicked.connect(self.gotoLogin)
        self.create.clicked.connect(self.gotoCreate)

    def gotoLogin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoCreate(self):
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("UI/login.ui", self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginFunction)

    def loginFunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()

        if len(user) == 0 or len(password) == 0:
            self.error.setText("Please input all fields.")

        else:
            if aggregator.login(user, password):
                self.gotoChoiceOfAction()
                #self.gotoMainWindow()
                print("Successfully logged in.")
                self.error.setText("")
            else:
                self.error.setText("Invalid username or password")

    def gotoChoiceOfAction(self):
        choiceOfAction = ChoiceOfAction()
        self.login.clicked.connect(self.gotoChoiceOfAction)
        widget.addWidget(choiceOfAction)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoMainWindow(self):
        mainWindow = MainWindow()
        self.login.clicked.connect(self.gotoMainWindow)
        widget.addWidget(mainWindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ChoiceOfAction(QDialog):
    def __init__(self):
        super(ChoiceOfAction, self).__init__()
        loadUi("UI/choiceofaction.ui", self)
        self.listFilms.clicked.connect(self.displayList)

    def displayList(self):
        listFilms = ListFilms()
        self.listFilms.clicked.connect(self.displayList)
        widget.addWidget(listFilms)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ListFilms(QDialog, QListWidget):
    def __init__(self):
        super(ListFilms, self).__init__()
        self.resize(1200, 800)
        self.setStyleSheet('font-size: 40px')
        loadUi("UI/films.ui", self)
        content_list = aggregator.get_content_list()
        list_films = content_list.list_films

        ##list_tv_shows = content_list.list_tv_shows
        for film in list_films:
            self.listFilms.addItem(film.name)

        ##self.listFilms.setResizeMode(QListWidget.)
        ##self.listFilms.takeItem()
        self.addRating.clicked.connect(self.addSelRating)
        self.listFilms.itemDoubleClicked.connect(self.launchPopup)
        print(aggregator.user.get_rating_list_film()[0]['rating_user'])

    def addSelRating(self):
        ##rating = self.spinRating.int()
        print(self.listFilms.selectedItems())

    def launchPopup(self, item):
        content_list = aggregator.get_content_list()
        list_films = content_list.list_films
        for film in list_films:
            if film.name == item.text():
                pop = Popup(film, self)
                pop.show()


class Popup(QDialog, QListWidget):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.resize(1200, 800)
        self.labelTitle = QLabel('Подробнее о фильме', self)
        self.labelTitle.setGeometry(QtCore.QRect(0, 0, 1000, 71))
        self.labelName = QLabel('Название фильма: ' + name.name, self)
        self.labelName.setGeometry(QtCore.QRect(0, 100, 1000, 71))
        self.labelGenre = QLabel('Жанр: ' + name.genre, self)
        self.labelGenre.setGeometry(QtCore.QRect(0, 150, 1000, 71))
        self.labelDescription = QLabel('Описание: ' + name.description, self)
        self.labelDescription.setGeometry(QtCore.QRect(0, 200, 2000, 71))
        self.labelCountry = QLabel('Страна: ' + name.country, self)
        self.labelCountry.setGeometry(QtCore.QRect(0, 250, 2000, 71))
        self.labelYear = QLabel('Год: ' + str(name.year), self)
        self.labelYear.setGeometry((QtCore.QRect(0, 300, 2000, 71)))
        self.labelRating = QLabel('Рейтинг: ' + str(name.rating), self)
        self.labelRating.setGeometry(QtCore.QRect(0, 350, 2000, 71))
        self.labelDirector = QLabel('Режиссер: ' + name.director, self)
        self.labelDirector.setGeometry(QtCore.QRect(0, 400, 2000, 71))
        self.labelDuration = QLabel('Длительность: ' + str(name.duration)+'min', self)
        self.labelDuration.setGeometry(QtCore.QRect(0, 450, 2000, 71))
        self.labelBudget = QLabel('Бюджет: ' + str(name.budget)+'$', self)
        self.labelBudget.setGeometry(QtCore.QRect(0, 500, 2000, 71))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("UI/mainwindow.ui", self)

        # lst = ['123', 'vcdf']
        # Items List
        # self.listWidget = QListWidget()
        # self.listWidget_2 = QListWidget()
        # for el in lst:
        #     self.listWidget.addItem(el)
        # for el in lst:
        #     self.listWidget_2.addItem(el)
        # self.listWidget_2.itemClicked.connect(self.launchPopup)
        # for film in aggregator.contentList.listFilms:
        #     self.addItem(film)
        #
        # self.itemDoubleClicked.connect(self.launchPopup)

#     def launchPopup(self, item):
#         pop = Popup(item.name.text(), self)
#         pop.show()
#
#
# class Popup(QDialog):
#     def __init__(self, name, parent):
#         super().__init__(parent)
#         self.resize(600, 300)
#         self.label = QLabel(name, self)


class CreateAccScreen(QDialog):
    def __init__(self):
        super(CreateAccScreen, self).__init__()
        loadUi("UI/createacc.ui", self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.signupFunction)

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
                print("User with this name is already registered")

    def gotoLogin(self):
        login = LoginScreen()
        self.signup.clicked.connect(self.gotoLogin)
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# main
aggregator = Aggregator(host, userDb, passwordDb, db_name)
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
