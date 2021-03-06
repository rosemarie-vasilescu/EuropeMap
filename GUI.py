# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import time

from astar import astar
from bfs import bfs

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cmbSrc = QtWidgets.QComboBox(self.centralwidget)
        self.cmbSrc.setGeometry(QtCore.QRect(40, 60, 151, 22))
        self.cmbSrc.setObjectName("cmbSrc")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 151, 16))
        self.label.setObjectName("label")
        self.cmbDest = QtWidgets.QComboBox(self.centralwidget)
        self.cmbDest.setGeometry(QtCore.QRect(50, 130, 141, 22))
        self.cmbDest.setObjectName("cmbDest")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 141, 16))
        self.label_2.setObjectName("label_2")
        self.btnBFS = QtWidgets.QPushButton(self.centralwidget)
        self.btnBFS.setGeometry(QtCore.QRect(50, 180, 93, 28))
        self.btnBFS.setObjectName("btnBFS")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 60, 55, 16))
        self.label_3.setObjectName("label_3")
        self.lblPath = QtWidgets.QLabel(self.centralwidget)
        self.lblPath.setGeometry(QtCore.QRect(310, 90, 55, 16))
        self.lblPath.setText("")
        self.lblPath.setObjectName("lblPath")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 140, 121, 16))
        self.label_4.setObjectName("label_4")
        self.lblVizitate = QtWidgets.QLabel(self.centralwidget)
        self.lblVizitate.setGeometry(QtCore.QRect(310, 180, 55, 16))
        self.lblVizitate.setText("")
        self.lblVizitate.setObjectName("lblVizitate")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 230, 121, 16))
        self.label_5.setObjectName("label_5")
        self.lblNrViz = QtWidgets.QLabel(self.centralwidget)
        self.lblNrViz.setGeometry(QtCore.QRect(310, 270, 55, 16))
        self.lblNrViz.setText("")
        self.lblNrViz.setObjectName("lblNrViz")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 310, 131, 16))
        self.label_6.setObjectName("label_6")
        self.lblLungime = QtWidgets.QLabel(self.centralwidget)
        self.lblLungime.setGeometry(QtCore.QRect(310, 350, 55, 16))
        self.lblLungime.setText("")
        self.lblLungime.setObjectName("lblLungime")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 380, 111, 16))
        self.label_7.setObjectName("label_7")
        self.lblDistanta = QtWidgets.QLabel(self.centralwidget)
        self.lblDistanta.setGeometry(QtCore.QRect(310, 410, 55, 16))
        self.lblDistanta.setText("")
        self.lblDistanta.setObjectName("lblDistanta")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(310, 430, 111, 16))
        self.label_8.setObjectName("label_8")
        self.lblTimp = QtWidgets.QLabel(self.centralwidget)
        self.lblTimp.setGeometry(QtCore.QRect(310, 450, 55, 16))
        self.lblTimp.setText("")
        self.lblTimp.setObjectName("lblTimp")
        self.btnAstar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAstar.setGeometry(QtCore.QRect(160, 180, 93, 28))
        self.btnAstar.setObjectName("btnAstar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.loadCmb()
        self.cmbSrc.addItems(self.city)
        self.cmbDest.addItems(self.city)
        self.btnAstar.clicked.connect(self.executaAstar)
        self.btnBFS.clicked.connect(self.executaBFS)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Alegeti orasul de pornire"))
        self.label_2.setText(_translate("MainWindow", "Alegeti orasul destinatie"))
        self.btnBFS.setText(_translate("MainWindow", "BFS"))
        self.label_3.setText(_translate("MainWindow", "Ruta"))
        self.label_4.setText(_translate("MainWindow", "Lista orase vizitate"))
        self.label_5.setText(_translate("MainWindow", "Numar orase vizitate"))
        self.label_6.setText(_translate("MainWindow", "Lungime cale finala "))
        self.label_7.setText(_translate("MainWindow", "Distanta totala"))
        self.label_8.setText(_translate("MainWindow", "Timp executie"))

        self.btnAstar.setText(_translate("MainWindow", "A*"))

    def loadCmb(self):

        file = open("D:\Facultate\Anul 3\IA\city.txt", 'r')
        n = int(file.readline())
        # n = len(file.readlines())
        print(n)
        self.city = []
        for i in range(n - 1):
            line = file.readline().split(',')

            ct1 = line[0]
            ct1 = ct1.strip('\n')
            self.city.append(ct1)
        print(self.city)

    def incarcaAstar(self):
        print("incarca")
        with open("C:\\Users\\rosem\PycharmProjects\\romaniaMap\\astar.txt", 'r') as file:
            for line in file:
                line = line.strip().split("#")
                self.finalpath = line[0].strip()
                self.lungime = line[1].strip()
                self.cost = line[2].strip()
                self.vizitat = line[3].strip()
                self.nrviz = line[4].strip()

    def incarcaBFS(self):
        print("incarca")
        with open("C:\\Users\\rosem\PycharmProjects\\romaniaMap\\bfs.txt", 'r') as file:
            for line in file:
                line = line.strip().split("#")
                self.finalpath = line[0].strip()
                self.lungime = line[1].strip()
                self.vizitat = line[2].strip()
                self.nrviz = line[3].strip()
                self.cost = line[4].strip()


    def executaBFS(self):
        print("executa bfs")
        self.src = self.findSrc()
        self.dest = self.findDest()
        # self.src = "Bucharest"
        # self.dest = "London"
        print(self.src)
        print(self.dest)
        tic = time.perf_counter()
        bfs(self.src, self.dest)
        toc = time.perf_counter()
        timp = toc - tic

        self.incarcaBFS()
        print(str(self.finalpath))
        print(str(len(self.finalpath)))
        print(str(self.vizitat))
        print(str(len(self.vizitat)))
        # print(str(self.cost))
        path = self.finalpath.replace("[","").replace("]","").replace("'","")
        self.lblPath.setText(str(path))
        self.lblPath.adjustSize()
        self.lblLungime.setText(str(self.lungime))
        path1 = self.vizitat.replace("[", "").replace("]", "").replace("'", "")
        self.lblVizitate.setText(str(path1))
        self.lblVizitate.adjustSize()
        self.lblNrViz.setText(str(self.nrviz))
        self.lblDistanta.setText(str(self.cost))
        self.lblTimp.setText((str(timp)))
        self.lblTimp.adjustSize()
    def executaAstar(self):
        print("executa astar")
        self.src = self.findSrc()
        self.dest = self.findDest()
        # self.src = "Bucharest"
        # self.dest = "London"
        print(self.src)
        print(self.dest)
        tic = time.perf_counter()
        astar(self.src, self.dest)
        toc = time.perf_counter()
        timp = toc - tic

        self.incarcaAstar()
        print(str(self.finalpath))
        print(str(len(self.finalpath)))
        print(str(self.vizitat))
        print(str(len(self.vizitat)))
        print(str(self.cost))
        path = self.finalpath.replace("[","").replace("]","").replace("'","")
        self.lblPath.setText(str(path))
        self.lblPath.adjustSize()
        self.lblLungime.setText(str(self.lungime))
        path1 = self.vizitat.replace("[", "").replace("]", "").replace("'", "")
        self.lblVizitate.setText(str(path1))
        self.lblVizitate.adjustSize()
        self.lblNrViz.setText(str(self.nrviz))
        self.lblDistanta.setText(str(self.cost))
        self.lblTimp.setText((str(timp)))
        self.lblTimp.adjustSize()

    def findSrc(self):

       return self.cmbSrc.currentText()

    def findDest(self):

        return self.cmbDest.currentText()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
