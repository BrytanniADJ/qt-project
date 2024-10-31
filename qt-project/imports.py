# imports mínimos
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QTimer
# def. do APP
app = QtWidgets.QApplication([])

# iniciar aplicativo
app.exec_()

# Objetivo:
#   Recriar as telas e fazê-las funcionar em ordem;
#   Não tem limite de linhas de código;
#   Tente recriar as telas parecidas com os prints;
#   Pode colocar mais imports se achar necessário;
#   Todos os botões precisam estar funcionando [exceto os botões da última tela (login)].

# Opcional: Da primeira até a segunda tela, não irá necessitar de botão,
# o aplicativo deve passar da tela 1 até a tela 2 automaticamente depois
# de alguns segundos.