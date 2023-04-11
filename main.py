from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QMainWindow,QGraphicsColorizeEffect
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QCoreApplication,QTimer
from PyQt5.QtGui import *
import sys
import res
import webbrowser
import pyrebase
import urllib.request
import requests

firebaseConfig = {
  'apiKey': "AIzaSyAyq6zsOfwz3j7oz1zOnJdONJoke78VaYo",
  'authDomain': "zeonapp-74e4a.firebaseapp.com",
  'databaseURL': "https://zeonapp-74e4a.firebaseip.com",
  'projectId': "zeonapp-74e4a",
  'storageBucket': "zeonapp-74e4a.appspot.com",
  'messagingSenderId': "753419177169",
  'appId': "1:753419177169:web:d383c9c57a88cc267bc9f0"
  }

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db=firebase.database()

class main_window(QMainWindow):
    def __init__(self):
        super(main_window,self).__init__()
        loadUi("main_window.ui",self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.btn_discord.clicked.connect(self.opendc)
        self.btn_sponsor.clicked.connect(self.openspn)
        self.btn_facebook.clicked.connect(self.openfb)
        self.btn_instagram.clicked.connect(self.openins)
        self.btn_youtube.clicked.connect(self.openyt)
        self.btn_twitter.clicked.connect(self.opentwit)
        self.btn_twitch.clicked.connect(self.opentw)
        self.btn_quit.clicked.connect(self.quitw)
        self.btn_hide.clicked.connect(self.bhide)
        self.btn_announcements.clicked.connect(self.announcementsw)
        self.btn_settings.clicked.connect(self.settingsw)
        self.btn_notifications.clicked.connect(self.notificationsw)
        self.btn_pictures_1.clicked.connect(self.p1)
        self.btn_pictures_2.clicked.connect(self.p2)
        self.btn_pictures_3.clicked.connect(self.p3)
        self.btn_pictures_4.clicked.connect(self.p4)
        self.btn_pictures_5.clicked.connect(self.p5)

        cloudfilename="pictures1.png"
        url=firebase.storage().child(cloudfilename).get_url(None)
        image = QImage()
        image.loadFromData(requests.get(url).content)
        self.lbl_pictures.setPixmap(QPixmap(image))
        
    def p1(self):
        cloudfilename="pictures1.png"
        url=firebase.storage().child(cloudfilename).get_url(None)
        image = QImage()
        image.loadFromData(requests.get(url).content)
        self.lbl_pictures.setPixmap(QPixmap(image))

    def p2(self):
        cloudfilename="pictures2.png"
        url=firebase.storage().child(cloudfilename).get_url(None)
        image = QImage()
        image.loadFromData(requests.get(url).content)
        self.lbl_pictures.setPixmap(QPixmap(image))

    def p3(self):
        cloudfilename="pictures3.png"
        url=firebase.storage().child(cloudfilename).get_url(None)
        image = QImage()
        image.loadFromData(requests.get(url).content)
        self.lbl_pictures.setPixmap(QPixmap(image))

    def p4(self):
        cloudfilename="pictures4.png"
        url=firebase.storage().child(cloudfilename).get_url(None)
        image = QImage()
        image.loadFromData(requests.get(url).content)
        self.lbl_pictures.setPixmap(QPixmap(image))

    def p5(self):
        cloudfilename="pictures5.png"
        url=firebase.storage().child(cloudfilename).get_url(None)
        image = QImage()
        image.loadFromData(requests.get(url).content)
        self.lbl_pictures.setPixmap(QPixmap(image))

    def opendc(self):
        webbrowser.open('https://discord.com/invite/zeon')

    def openspn(self):
        webbrowser.open('https://www.kabasakalonline.com/?referans=zeonnn')

    def openfb(self):
        webbrowser.open('https://www.facebook.com/zeon')

    def openins(self):
        webbrowser.open('https://www.instagram.com/necatiakcay/')

    def openyt(self):
        webbrowser.open('https://www.youtube.com/user/NecatiAkcay')

    def opentwit(self):
        webbrowser.open('https://twitter.com/NecatiAkcay')

    def opentw(self):
        webbrowser.open('https://www.twitch.tv/zeon')

    def quitw(self):
        self.openw = quit_window()
        self.openw.show()
    
    def announcementsw(self):
        self.close()
        self.openw = announcements()
        self.openw.show()

    def bhide(self):
        self.showMinimized()

    def settingsw(self):
        self.openw = settings_window()
        self.openw.show()

    def notificationsw(self):
        self.openw = notifications_window()
        self.openw.show()

class announcements(QMainWindow):
    def __init__(self):
        super(announcements,self).__init__()
        loadUi("announcements.ui",self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.btn_home.clicked.connect(self.mainw)
        self.btn_quit.clicked.connect(self.quitw)
        self.btn_news_1.clicked.connect(self.news1)
        self.btn_news_2.clicked.connect(self.news2)
        self.btn_news_3.clicked.connect(self.news3)
        self.btn_news_4.clicked.connect(self.news4)
        self.btn_news_5.clicked.connect(self.news5)

        cloudfilename="news1.txt"
        url=firebase.storage().child(cloudfilename).get_url(None)
        file = urllib.request.urlopen(url)
        self.lbl_text.setText(str(file.read(),'utf-8'))
        self.lbl_text.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_text.setFont(QFont('Bahnschrift',10))
        color_effect = QGraphicsColorizeEffect()
        color_effect.setColor(QtCore.Qt.white)
        self.lbl_text.setGraphicsEffect(color_effect)

    def mainw(self):
        self.close()
        self.openw = main_window()
        self.openw.show()

    def quitw(self):
        self.openw = quit_window()
        self.openw.show()

    def news1(self):
        cloudfilename="news1.txt"
        url=firebase.storage().child(cloudfilename).get_url(None)
        file = urllib.request.urlopen(url)
        self.lbl_text.setText(str(file.read(),'utf-8'))
        self.lbl_text.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_text.setFont(QFont('Bahnschrift',10))
        color_effect = QGraphicsColorizeEffect()
        color_effect.setColor(QtCore.Qt.white)
        self.lbl_text.setGraphicsEffect(color_effect)

    def news2(self):
        cloudfilename="news2.txt"
        url=firebase.storage().child(cloudfilename).get_url(None)
        file = urllib.request.urlopen(url)
        self.lbl_text.setText(str(file.read(),'utf-8'))
        self.lbl_text.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_text.setFont(QFont('Bahnschrift',10))
        color_effect = QGraphicsColorizeEffect()
        color_effect.setColor(QtCore.Qt.white)
        self.lbl_text.setGraphicsEffect(color_effect)

    def news3(self):
        cloudfilename="news3.txt"
        url=firebase.storage().child(cloudfilename).get_url(None)
        file = urllib.request.urlopen(url)
        self.lbl_text.setText(str(file.read(),'utf-8'))
        self.lbl_text.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_text.setFont(QFont('Bahnschrift',10))
        color_effect = QGraphicsColorizeEffect()
        color_effect.setColor(QtCore.Qt.white)
        self.lbl_text.setGraphicsEffect(color_effect)

    def news4(self):
        cloudfilename="news4.txt"
        url=firebase.storage().child(cloudfilename).get_url(None)
        file = urllib.request.urlopen(url)
        self.lbl_text.setText(str(file.read(),'utf-8'))
        self.lbl_text.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_text.setFont(QFont('Bahnschrift',10))
        color_effect = QGraphicsColorizeEffect()
        color_effect.setColor(QtCore.Qt.white)
        self.lbl_text.setGraphicsEffect(color_effect)

    def news5(self):
        cloudfilename="news5.txt"
        url=firebase.storage().child(cloudfilename).get_url(None)
        file = urllib.request.urlopen(url)
        self.lbl_text.setText(str(file.read(),'utf-8'))
        self.lbl_text.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_text.setFont(QFont('Bahnschrift',10))
        color_effect = QGraphicsColorizeEffect()
        color_effect.setColor(QtCore.Qt.white)
        self.lbl_text.setGraphicsEffect(color_effect)

class settings_window(QMainWindow):
    def __init__(self):
        super(settings_window,self).__init__()
        loadUi("settings.ui",self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.btn_quit.clicked.connect(self.close_settings)

    def close_settings(self):
        self.close()

class notifications_window(QMainWindow):
    def __init__(self):
        super(notifications_window,self).__init__()
        loadUi("notifications.ui",self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.btn_quit.clicked.connect(self.close_settings)

    
        cloudfilename="not1.txt"
        url=firebase.storage().child(cloudfilename).get_url(None)
        file = urllib.request.urlopen(url)
        self.lbl_not1.setText(str(file.read(),'utf-8'))
        self.lbl_not1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_not1.setFont(QFont('Bahnschrift',10))
        color_effect = QGraphicsColorizeEffect()
        color_effect.setColor(QtCore.Qt.white)
        self.lbl_not1.setGraphicsEffect(color_effect)

        cloudfilename="not2.txt"
        url=firebase.storage().child(cloudfilename).get_url(None)
        file = urllib.request.urlopen(url)
        self.lbl_not2.setText(str(file.read(),'utf-8'))
        self.lbl_not2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_not2.setFont(QFont('Bahnschrift',10))
        color_effect = QGraphicsColorizeEffect()
        color_effect.setColor(QtCore.Qt.white)
        self.lbl_not2.setGraphicsEffect(color_effect)

        cloudfilename="not3.txt"
        url=firebase.storage().child(cloudfilename).get_url(None)
        file = urllib.request.urlopen(url)
        self.lbl_not3.setText(str(file.read(),'utf-8'))
        self.lbl_not3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_not3.setFont(QFont('Bahnschrift',10))
        color_effect = QGraphicsColorizeEffect()
        color_effect.setColor(QtCore.Qt.white)
        self.lbl_not3.setGraphicsEffect(color_effect)

        cloudfilename="not4.txt"
        url=firebase.storage().child(cloudfilename).get_url(None)
        file = urllib.request.urlopen(url)
        self.lbl_not4.setText(str(file.read(),'utf-8'))
        self.lbl_not4.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_not4.setFont(QFont('Bahnschrift',10))
        color_effect = QGraphicsColorizeEffect()
        color_effect.setColor(QtCore.Qt.white)
        self.lbl_not4.setGraphicsEffect(color_effect)

    def close_settings(self):
        self.close()
        
class quit_window(QMainWindow):
    def __init__(self):
        super(quit_window,self).__init__()
        loadUi("quit_window.ui",self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.btn_yes.clicked.connect(self.yes)
        self.btn_no.clicked.connect(self.no)

    def yes(self):
        QCoreApplication.instance().quit()

    def no(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec_())



