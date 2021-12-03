from PyQt5 import QtNetwork
from PyQt5.QtCore import QCoreApplication, QUrl
import sys


class HttpClient:

    def __init__(self):

        self.nam = QtNetwork.QNetworkAccessManager()
        self.getRequest()

    def getRequest(self):
        '''Запрос на получение коллекции'''
        url = ''
        req = QtNetwork.QNetworkRequest(QUrl(url))

        self.nam.finished.connect(self.handleResponse)
        self.nam.get(req)

    @staticmethod
    def handleResponse(reply):

        er = reply.error()

        if er != QtNetwork.QNetworkReply.NetworkError:

            bytes_string = reply.readAll()
            print(str(bytes_string, 'utf-8'))

        else:
            print("Error occured: ", er)
            print(reply.errorString())

        QCoreApplication.quit()

## client = HttpClient()