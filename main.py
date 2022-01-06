# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import http.server
import socketserver
import random
import os
import socket
import argparse
import sys
from shutil import make_archive, move, rmtree, copy2
import pathlib
from PIL import Image

import sys
from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(QMainWindow):
    # Obtener ip local predeterminada
    def get_local_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

# Generar un puerto aleatorio
    def random_port():
        return random.randint(1024, 65535)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
                                 "background-color:rgb(38, 50, 56);\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_qr = QFrame(self.centralwidget)
        self.frame_qr.setObjectName(u"frame_qr")
        self.frame_qr.setGeometry(QRect(590, 190, 260, 260))
        self.frame_qr.setStyleSheet(u"QFrame{\n"
                                    "background-color: rgb(24, 36, 43);\n"
                                    "border-radius: 10px;\n"
                                    "}")
        self.frame_qr.setFrameShape(QFrame.StyledPanel)
        self.frame_qr.setFrameShadow(QFrame.Raised)
        self.label_qr = QLabel(self.centralwidget)
        self.label_qr.setObjectName(u"label_qr")
        self.label_qr.setGeometry(QRect(590, 149, 260, 31))
        font = QFont()
        font.setFamily(u"Ubuntu")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_qr.setFont(font)
        self.label_qr.setStyleSheet(u"QLabel{\n"
                                    "border-radius: 10px;\n"
                                    "background-color: rgb(24, 36, 43);\n"
                                    "color : rgb(132, 201, 251);\n"
                                    "}")
        self.label_qr.setAlignment(Qt.AlignCenter)
        self.label_titulo = QLabel(self.centralwidget)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setGeometry(QRect(50, 30, 800, 63))
        font1 = QFont()
        font1.setFamily(u"Ubuntu")
        font1.setPointSize(23)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_titulo.setFont(font1)
        self.label_titulo.setStyleSheet(u"QLabel{\n"
                                        "border-radius: 25px;\n"
                                        "background-color: rgb(24, 36, 43);\n"
                                        "color : rgb(132, 201, 251);\n"
                                        "}")
        self.label_titulo.setAlignment(Qt.AlignCenter)
        self.pushButton_archivo = QPushButton(self.centralwidget)
        self.pushButton_archivo.setObjectName(u"pushButton_archivo")
        self.pushButton_archivo.setGeometry(QRect(80, 150, 400, 35))
        font2 = QFont()
        font2.setFamily(u"Ubuntu")
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(75)
        self.pushButton_archivo.setFont(font2)
        self.pushButton_archivo.setStyleSheet(u"QPushButton{\n"
                                              "background-color: rgb(0, 131, 143);\n"
                                              "border-radius: 10px;\n"
                                              "color: rgb(224, 247, 250);\n"
                                              "}")
        self.pushButton_enviar = QPushButton(self.centralwidget)
        self.pushButton_enviar.setObjectName(u"pushButton_enviar")
        self.pushButton_enviar.setGeometry(QRect(80, 200, 400, 35))
        self.pushButton_enviar.setFont(font)
        self.pushButton_enviar.setStyleSheet(u"QPushButton{\n"
                                             "background-color: rgb(85, 139, 47);\n"
                                             "color: rgb(169, 215, 137);\n"
                                             "border-radius: 10px;\n"
                                             "}")
        self.pushButton_salir = QPushButton(self.centralwidget)
        self.pushButton_salir.setObjectName(u"pushButton_salir")
        self.pushButton_salir.setGeometry(QRect(590, 520, 260, 35))
        self.pushButton_salir.setFont(font)
        self.pushButton_salir.setStyleSheet(u"QPushButton{\n"
                                            "background-color:rgb(173, 20, 87);\n"
                                            "color: rgb(244, 143, 177);\n"
                                            "border-radius: 10px;\n"
                                            "}")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(80, 350, 400, 200))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit{\n"
                                         "background-color: rgb(24, 36, 43);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius: 10px;\n"
                                         "}")
        self.label_ip = QLabel(self.centralwidget)
        self.label_ip.setObjectName(u"label_ip")
        self.label_ip.setGeometry(QRect(80, 250, 190, 35))
        font3 = QFont()
        font3.setFamily(u"Ubuntu")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_ip.setFont(font3)
        self.label_ip.setStyleSheet(u"QLabel{\n"
                                    "border-radius: 10px;\n"
                                    "background-color: rgb(24, 36, 43);\n"
                                    "color : rgb(132, 201, 251);\n"
                                    "}")
        self.label_ip.setAlignment(Qt.AlignCenter)
        self.label_puerto = QLabel(self.centralwidget)
        self.label_puerto.setObjectName(u"label_puerto")
        self.label_puerto.setGeometry(QRect(290, 250, 190, 35))
        self.label_puerto.setFont(font3)
        self.label_puerto.setStyleSheet(u"QLabel{\n"
                                        "border-radius: 10px;\n"
                                        "background-color: rgb(24, 36, 43);\n"
                                        "color : rgb(132, 201, 251);\n"
                                        "}")
        self.label_puerto.setAlignment(Qt.AlignCenter)
        self.label_nom_archivo = QLabel(self.centralwidget)
        self.label_nom_archivo.setObjectName(u"label_nom_archivo")
        self.label_nom_archivo.setGeometry(QRect(80, 300, 400, 35))
        self.label_nom_archivo.setFont(font3)
        self.label_nom_archivo.setStyleSheet(u"QLabel{\n"
                                             "border-radius: 10px;\n"
                                             "background-color: rgb(24, 36, 43);\n"
                                             "color : rgb(132, 201, 251);\n"
                                             "}")
        self.label_nom_archivo.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_archivo.clicked.connect(self.obtenerRuta)
    # setupUi

    def obtenerRuta(self):
        ip = get_local_ip()
        # Open file dialog
        fname = QFileDialog.getOpenFileName(
            self, "Selecciona el archivo", "", "All files (*)")
        #fname = QFileDialog.getExistingDirectory()
        if fname:
            self.plainTextEdit.setPlainText(fname[0])

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.label_qr.setText(QCoreApplication.translate(
            "MainWindow", u"CODIGO QR GENERADO", None))
        self.label_titulo.setText(QCoreApplication.translate(
            "MainWindow", u"Transferencia de archivos", None))
        self.pushButton_archivo.setText(QCoreApplication.translate(
            "MainWindow", u"Seleccionar archivo / directorio", None))
        self.pushButton_enviar.setText(QCoreApplication.translate(
            "MainWindow", u"T R A N S F E R I R", None))
        self.pushButton_salir.setText(
            QCoreApplication.translate("MainWindow", u"SALIR", None))
        self.label_ip.setText(
            QCoreApplication.translate("MainWindow", u"IP:", None))
        self.label_puerto.setText(
            QCoreApplication.translate("MainWindow", u"Puerto:", None))
        self.label_nom_archivo.setText(QCoreApplication.translate(
            "MainWindow", u"Nombre del archivo:", None))
    # retranslateUi


if __name__ == "__main__":
    # create a new instance of QApplication
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()  # create a new instance of the Ui you just cerated.
    w = QtWidgets.QMainWindow()  # create an instance of QMainWindow
    ex.setupUi(w)  # create your widgets inside the window you just created.
    w.show()  # show the window.
    sys.exit(app.exec_())
