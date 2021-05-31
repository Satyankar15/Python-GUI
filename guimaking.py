# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 20:16:13 2020

@author: satya
"""

from qtpy import QtWidgets
from qtpy.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app= QApplication(sys.argv)
    win= QMainWindow()
    win.setGeometry(200,200,300,300)
    win.setWindowTitle("Window Title")
    
    label=QtWidgets.QLabel(win)
    label.setText("Sample text")
    label.move(50,50)
    
    b1=QtWidgets.QPushButton(win)
    b1.setText("Click me")
    b1.clicked.connect(clicked)
    
    win.show()
    sys.exit(app.exec_())

def clicked():
    print("Button clicked")   

window()