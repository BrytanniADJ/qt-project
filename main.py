# principais Imports
import sys
from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QApplication, QErrorMessage
from PyQt6.QtCore import QTimer
import mysql.connector
from mysql.connector import Error
from datetime import datetime
import threading
from PyQt5 import QtWidgets, QtCore 
# Imports à parte
from fpdf import FPDF
import os
from PyQt6 import QtWidgets
# Iniciar plicativo
app = QtWidgets.QApplication([])

def pular_tutorial():
    login.show()
    tutorial_pt1.close()
    tutorial_pt2.close()
    tutorial_pt3.close()

def nextPage1():
    tutorial_pt1.show()
    tutorial_pt2.close()

def nextPage2():
    tutorial_pt2.show()
    tutorial_pt1.close()
    tutorial_pt3.close()


# Parte de login
login = uic.loadUi('telas/loginwindow.ui')

# tutorial / páginas inciais
main = uic.loadUi('telas/mainwindow.ui')
tutorial_pt1 = uic.loadUi('telas/tutorial1.ui')
tutorial_pt2 = uic.loadUi('telas/tutorial2.ui')
tutorial_pt3 = uic.loadUi('telas/tutorial3.ui')
# botão pular tutorial
tutorial_pt1.pushJump.clicked.connect(pular_tutorial)
tutorial_pt2.pushJump.clicked.connect(pular_tutorial)
tutorial_pt3.pushJump.clicked.connect(pular_tutorial)
# next e jump
tutorial_pt1.pushNext.clicked.connect(nextPage2) # tutorial 2
tutorial_pt3.pushBack.clicked.connect(nextPage2)

tutorial_pt1.show()
app.exec()