# -*- coding: utf-8 -*-
"""
Created on Thu May 18 16:28:05 2023

@author: Irene
"""
import sys
from PyQt5 import QtWidgets

from GUI.mainwindow import MyApp

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())