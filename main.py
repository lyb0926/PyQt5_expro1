# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.py'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
import contr
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = contr.MyWidgets()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())