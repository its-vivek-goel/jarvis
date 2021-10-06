#this file is use to run the gui application

from jarvis import jarvis
import sys 
import datetime
import time


from jarvis import jarvis

from PyQt5 import QtWidgets , QtCore , QtGui
from PyQt5.QtCore import QTimer , QTime , QDate , Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvis_ui import Ui_jarvisGui
from speak import speak

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        
        speak('System has initialised properly .. Your a i assistant is ready to use')
        speak('Speak jarvis or hey jarvis to use') 
        jarvis()                              #to start the main program 
        
startExecution = MainThread()                 #object of mainthread class


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisGui()
        self.ui.setupUi(self)
        self.ui.pushButton1.clicked.connect(self.startTask)


    def startTask(self):

        self.ui.pushButton1.hide()


        self.label3_load()
        self.label4_load()
        try:
            timer = QTimer(self)
            timer.timeout.connect(self.showTime)
            timer.start()
            
        except Exception as e :
            pass

        self.label2_load()
        self.label1_load()
        
        self.label6_load()
        self.label7_load()
        
        startExecution.start()

    def showTime(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M:%S %p")
        current_date = now.strftime("%d/%m/%y")
        self.ui.label5.setHidden(False)
        self.ui.textBrowser1.setText(current_time)
        self.ui.textBrowser2.setText(current_date)


    def label1_load(self):
        #to run the gui at label3
        self.ui.movie_l1 = QtGui.QMovie("img/1.gif")
        self.ui.label1.setMovie(self.ui.movie_l1)
        self.ui.movie_l1.start()

    def label2_load(self):
        #to run the gui at label3
        self.ui.label2.setHidden(False)        #making label 2 visible
        self.ui.movie_l2 = QtGui.QMovie("img/2.gif")
        self.ui.label2.setMovie(self.ui.movie_l2)
        self.ui.movie_l2.setSpeed(130)
        self.ui.movie_l2.start()


    def label3_load(self):                  #to load label 3
        #to speak 
        speak("Initializing System")
        #to run the gui at label3
        self.ui.label3.setHidden(False)        #making label 3 visible
        self.ui.movie_l3 = QtGui.QMovie("img/3.gif")
        self.ui.label3.setMovie(self.ui.movie_l3)
        self.ui.movie_l3.start()
        

    def label4_load(self):              #making label 4 visible

        speak("Please Hold on ,Loading Disks , Checking Security")
        speak("Launching User Interface")
        self.ui.label4.setHidden(False)        #making label 4 visible
        self.ui.movie_l4 = QtGui.QMovie("img/4.gif")
        self.ui.label4.setMovie(self.ui.movie_l4)
        self.ui.movie_l4.start()

    def label6_load(self):              #making label 6 visible

        self.ui.label6.setHidden(False)        #making label 6 visible
        self.ui.movie_l6 = QtGui.QMovie("img/6.gif")
        self.ui.label6.setMovie(self.ui.movie_l6)
        self.ui.movie_l6.setSpeed(50)
        self.ui.movie_l6.start()


    def label7_load(self):              #making label 7 visible

        self.ui.label7.setHidden(False)        #making label 7 visible
        self.ui.movie_l7 = QtGui.QMovie("img/6.gif")
        self.ui.label7.setMovie(self.ui.movie_l7)
        self.ui.movie_l7.setSpeed(50)
        self.ui.movie_l7.start()




    

app = QApplication(sys.argv)

jarvis1 = Main()
jarvis1.show()

exit(app.exec_())