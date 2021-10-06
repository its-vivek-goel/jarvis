# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final_jarvis_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jarvisGui(object):


    def setupUi(self, jarvisGui):
        jarvisGui.setObjectName("jarvisGui")
        jarvisGui.resize(1362, 739)
        self.centralwidget = QtWidgets.QWidget(jarvisGui)
        self.centralwidget.setObjectName("centralwidget")

#rotating arc gif
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(-30, -30, 1401, 771))
        self.label1.setStyleSheet("")
        self.label1.setText("")
        self.label1.setPixmap(QtGui.QPixmap("img/1.gif"))
        self.label1.setScaledContents(True)
        self.label1.setObjectName("label1")

#rotating iron man gif
        
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(1070, 480, 241, 231))
        self.label2.setText("")
        self.label2.setPixmap(QtGui.QPixmap("img/2.gif"))
        self.label2.setScaledContents(True)
        self.label2.setObjectName("label2")
        self.label2.setHidden(True)


#initialising system gif
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(0, 10, 371, 91))
        self.label3.setText("")
        self.label3.setPixmap(QtGui.QPixmap("img/3.gif"))
        self.label3.setObjectName("label3")
        self.label3.setHidden(True)

#running code gif
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(10, 480, 281, 231))
        self.label4.setText("")
        self.label4.setPixmap(QtGui.QPixmap("img/4.gif"))
        self.label4.setObjectName("label4")
        self.label4.setHidden(True)

#to display date time 
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(1100, 20, 261, 121))
        self.label5.setText("")
        self.label5.setPixmap(QtGui.QPixmap("img/5.jpg"))
        self.label5.setObjectName("label5")
        self.label5.setHidden(True)

#to display electronic wave left
        self.label6 = QtWidgets.QLabel(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(0, 230, 269, 241))
        self.label6.setText("")
        self.label6.setPixmap(QtGui.QPixmap("img/6.gif"))
        self.label6.setScaledContents(True)
        self.label6.setObjectName("label6")
        self.label6.setHidden(True)

#to display electronic wave right

        self.label7 = QtWidgets.QLabel(self.centralwidget)
        self.label7.setGeometry(QtCore.QRect(1070, 240, 291, 241))
        self.label7.setText("")
        self.label7.setPixmap(QtGui.QPixmap("jarvis pic/200.gif"))
        self.label7.setScaledContents(True)
        self.label7.setObjectName("label7")
        self.label7.setHidden(True)

#to display date
        self.textBrowser1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser1.setGeometry(QtCore.QRect(1140, 40, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser1.setFont(font)
        self.textBrowser1.setStyleSheet("background:transparent;\n"
"border-radius:null;\n"
"color:white;")
        self.textBrowser1.setObjectName("textBrowser1")

#to display time
        self.textBrowser2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser2.setGeometry(QtCore.QRect(1140, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser2.setFont(font)
        self.textBrowser2.setStyleSheet("background:transparent;\n"
"border-radius:null;\n"
"color:white;")
        self.textBrowser2.setObjectName("textBrowser2")

#to display developed by
        self.textBrowser3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser3.setGeometry(QtCore.QRect(10, 710, 171, 21))
        self.textBrowser3.setObjectName("textBrowser3")

#to display running code 
        self.textBrowser4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser4.setGeometry(QtCore.QRect(10, 120, 220, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser4.setFont(font)
        self.textBrowser4.setStyleSheet("background:transparent;\n"
"border-radius:null;\n"
"color:white;")
        self.textBrowser4.setObjectName("textBrowser4")
        
        

#to add scroll area
#         self.scrollArea1 = QtWidgets.QScrollArea(self.centralwidget)
#         self.scrollArea1.setGeometry(QtCore.QRect(10, 350, 231, 241))
#         self.scrollArea1.setStyleSheet("background:transparent;\n"
# "")
#         self.scrollArea1.setWidgetResizable(True)
#         self.scrollArea1.setObjectName("scrollArea1")
#         self.scrollAreaWidgetContents = QtWidgets.QWidget()
#         self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 229, 239))
#         self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
#         self.scrollArea1.setWidget(self.scrollAreaWidgetContents)

#adding button        
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(630, 330, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("background:rgb(78, 156, 234);\n")
        self.pushButton1.setObjectName("pushButton1")


        jarvisGui.setCentralWidget(self.centralwidget)

        self.retranslateUi(jarvisGui)
        QtCore.QMetaObject.connectSlotsByName(jarvisGui)




    def retranslateUi(self, jarvisGui):
        _translate = QtCore.QCoreApplication.translate
        jarvisGui.setWindowTitle(_translate("jarvisGui", "A.I. Assistant"))


        self.textBrowser3.setHtml(_translate("jarvisGui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">Developed by Vivek Kumar Goel</span></p></body></html>"))
        
        self.pushButton1.setText(_translate("jarvisGui", "START"))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jarvisGui = QtWidgets.QMainWindow()
    ui = Ui_jarvisGui()
    ui.setupUi(jarvisGui)
    jarvisGui.show()
    sys.exit(app.exec_())
