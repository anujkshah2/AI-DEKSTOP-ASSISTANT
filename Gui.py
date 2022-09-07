import atexit
import sys
from threading import Timer
from JaegerBdy import Ui_MainWindow
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QTimer,QTime,QDate
from PyQt5.uic import loadUiType
import enginefile


class MainThread(QThread):

    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        enginefile.takeCommand()
        enginefile.taskExecution()
        enginefile.wakeup()
         
startExe= MainThread()
class gui_start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui=Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.pushButton.clicked.connect(self.startTask)
        self.gui.pushButton_2.clicked.connect(self.close)
    

    def startTask(self):
        self.gui.movie=QtGui.QMovie("movie/eight.gif")
        self.gui.label_2.setMovie(self.gui.movie)
        self.gui.movie.start()

        self.gui.movie=QtGui.QMovie("movie/2RNb.gif")
        self.gui.label_3.setMovie(self.gui.movie)
        self.gui.movie.start()

        self.gui.movie=QtGui.QMovie("movie/four.gif")
        self.gui.label_4.setMovie(self.gui.movie)
        self.gui.movie.start()

        self.gui.movie=QtGui.QMovie("movie/six.gif")
        self.gui.label_5.setMovie(self.gui.movie)
        self.gui.movie.start()

        self.gui.movie=QtGui.QMovie("movie/two.gif")
        self.gui.label_6.setMovie(self.gui.movie)
        self.gui.movie.start()

        self.gui.movie=QtGui.QMovie("movie/nine.gif")
        self.gui.label_7.setMovie(self.gui.movie)
        self.gui.movie.start()

        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(999)
        startExe.start()
    
    def showTime(self):
       t_ime=QTime.currentTime()
       time=t_ime.toString()
       d_ate=QDate.currentDate()
       date=d_ate.toString()
       label=time
       label_date=date
       self.gui.textBrowser.setText(label_date)
       self.gui.textBrowser_2.setText(label)

    

GuiApp=QApplication(sys.argv)
alita_gui=gui_start()
alita_gui.show()
atexit(GuiApp.exec_())
