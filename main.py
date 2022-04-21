from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def main_app():
    app = QApplication(sys.argv)
    wind = QMainWindow()

    wind.setWindowTitle("Виджеты")
    wind.setGeometry(600,300, 700,500)    #отступ, размер


    text = QtWidgets.QLabel(wind)
    text.setText("oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
    text.move(100,50)
    text.adjustSize()

    button = QtWidgets.QPushButton(wind)
    button.setGeometry(300, 100, 100, 50)
    button.setText("Жамк")
    button.adjustSize()

    wind.show()
    sys.exit(app.exec_())

main_app()