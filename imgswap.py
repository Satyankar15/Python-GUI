# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imgswap.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Photos = QtWidgets.QLabel(self.centralwidget)
        self.Photos.setGeometry(QtCore.QRect(0, 0, 801, 421))
        self.Photos.setText("")
        self.Photos.setPixmap(QtGui.QPixmap("Regular expressions guide.jpg"))
        self.Photos.setScaledContents(True)
        self.Photos.setObjectName("Photos")
        self.RegEx = QtWidgets.QPushButton(self.centralwidget)
        self.RegEx.setGeometry(QtCore.QRect(0, 420, 391, 81))
        self.RegEx.setObjectName("RegEx")
        self.Geo = QtWidgets.QPushButton(self.centralwidget)
        self.Geo.setGeometry(QtCore.QRect(380, 420, 421, 81))
        self.Geo.setObjectName("Geo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.RegEx.clicked.connect(self.show_RegEx)
        self.Geo.clicked.connect(self.show_Geo)
        
    def show_RegEx(self):
            self.Photos.setPixmap(QtGui.QPixmap("Regular expressions guide.jpg"))
            
    def show_Geo(self):
            self.Photos.setPixmap(QtGui.QPixmap("geoload.png"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RegEx.setText(_translate("MainWindow", "RegEx"))
        self.Geo.setText(_translate("MainWindow", "Geo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

