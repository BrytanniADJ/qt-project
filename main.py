# principais Imports
from PyQt6 import uic, QtWidgets, QtCore
from PyQt6.QtCore import QTimer
# Imports à parte
from PyQt6.QtWidgets import QApplication, QErrorMessage
from mysql.connector import Error
from datetime import datetime
import mysql.connector
from fpdf import FPDF
import threading
import time
import sys
import os
# Iniciar plicativo
app = QtWidgets.QApplication([])

def iniciar_main():
    main.show()
    QTimer.singleShot(2000, nextPage1)

def pular_tutorial():
    login.show()
    tutorial_pt1.close()
    tutorial_pt2.close()
    tutorial_pt3.close()

def nextPage1():
    tutorial_pt1.show()
    tutorial_pt2.close()
    main.close()

def nextPage2():
    tutorial_pt2.show()
    tutorial_pt1.close()
    tutorial_pt3.close()

def nextPage3():
    tutorial_pt3.show()
    tutorial_pt2.close()

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
tutorial_pt2.pushBack.clicked.connect(nextPage1) # tutorial 1
tutorial_pt1.pushNext.clicked.connect(nextPage2) # tutorial 2
tutorial_pt3.pushBack.clicked.connect(nextPage2)
tutorial_pt2.pushNext.clicked.connect(nextPage3) # tutorial 3
tutorial_pt3.pushNext.clicked.connect(pular_tutorial) # sair do tutorial


iniciar_main()
app.exec()