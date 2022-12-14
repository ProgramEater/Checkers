from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.h1 = QtWidgets.QLabel(self.centralwidget)
        self.h1.setGeometry(QtCore.QRect(100, 100, 75, 75))
        self.h1.setMinimumSize(QtCore.QSize(71, 75))
        self.h1.setText("")
        self.h1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.h1.setObjectName("h1")
        self.g1 = QtWidgets.QLabel(self.centralwidget)
        self.g1.setGeometry(QtCore.QRect(175, 100, 75, 75))
        self.g1.setMinimumSize(QtCore.QSize(70, 75))
        self.g1.setText("")
        self.g1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.g1.setObjectName("g1")
        self.f1 = QtWidgets.QLabel(self.centralwidget)
        self.f1.setGeometry(QtCore.QRect(250, 100, 75, 75))
        self.f1.setMinimumSize(QtCore.QSize(71, 75))
        self.f1.setText("")
        self.f1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.f1.setObjectName("f1")
        self.e1 = QtWidgets.QLabel(self.centralwidget)
        self.e1.setGeometry(QtCore.QRect(325, 100, 75, 75))
        self.e1.setMinimumSize(QtCore.QSize(71, 75))
        self.e1.setText("")
        self.e1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.e1.setObjectName("e1")
        self.d1 = QtWidgets.QLabel(self.centralwidget)
        self.d1.setGeometry(QtCore.QRect(400, 100, 75, 75))
        self.d1.setMinimumSize(QtCore.QSize(70, 75))
        self.d1.setText("")
        self.d1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.d1.setObjectName("d1")
        self.c1 = QtWidgets.QLabel(self.centralwidget)
        self.c1.setGeometry(QtCore.QRect(475, 100, 75, 75))
        self.c1.setMinimumSize(QtCore.QSize(71, 75))
        self.c1.setText("")
        self.c1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.c1.setObjectName("c1")
        self.b1 = QtWidgets.QLabel(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(550, 100, 75, 75))
        self.b1.setMinimumSize(QtCore.QSize(70, 75))
        self.b1.setText("")
        self.b1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.b1.setObjectName("b1")
        self.a1 = QtWidgets.QLabel(self.centralwidget)
        self.a1.setGeometry(QtCore.QRect(625, 100, 75, 75))
        self.a1.setMinimumSize(QtCore.QSize(71, 75))
        self.a1.setText("")
        self.a1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.a1.setObjectName("a1")
        self.boardLabel = QtWidgets.QLabel(self.centralwidget)
        self.boardLabel.setGeometry(QtCore.QRect(50, 20, 47, 13))
        self.boardLabel.setText("")
        self.boardLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.boardLabel.setObjectName("boardLabel")
        self.a7 = QtWidgets.QLabel(self.centralwidget)
        self.a7.setGeometry(QtCore.QRect(625, 550, 75, 75))
        self.a7.setText("")
        self.a7.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.a7.setObjectName("a7")
        self.b6 = QtWidgets.QLabel(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(550, 475, 75, 75))
        self.b6.setText("")
        self.b6.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.b6.setObjectName("b6")
        self.c5 = QtWidgets.QLabel(self.centralwidget)
        self.c5.setGeometry(QtCore.QRect(475, 400, 75, 75))
        self.c5.setText("")
        self.c5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.c5.setObjectName("c5")
        self.d5 = QtWidgets.QLabel(self.centralwidget)
        self.d5.setGeometry(QtCore.QRect(400, 400, 75, 75))
        self.d5.setText("")
        self.d5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.d5.setObjectName("d5")
        self.c4 = QtWidgets.QLabel(self.centralwidget)
        self.c4.setGeometry(QtCore.QRect(475, 325, 75, 75))
        self.c4.setText("")
        self.c4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.c4.setObjectName("c4")
        self.f5 = QtWidgets.QLabel(self.centralwidget)
        self.f5.setGeometry(QtCore.QRect(250, 400, 75, 75))
        self.f5.setText("")
        self.f5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.f5.setObjectName("f5")
        self.g6 = QtWidgets.QLabel(self.centralwidget)
        self.g6.setGeometry(QtCore.QRect(175, 475, 75, 75))
        self.g6.setText("")
        self.g6.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.g6.setObjectName("g6")
        self.g4 = QtWidgets.QLabel(self.centralwidget)
        self.g4.setGeometry(QtCore.QRect(175, 325, 75, 75))
        self.g4.setText("")
        self.g4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.g4.setObjectName("g4")
        self.a2 = QtWidgets.QLabel(self.centralwidget)
        self.a2.setGeometry(QtCore.QRect(625, 175, 75, 75))
        self.a2.setText("")
        self.a2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.a2.setObjectName("a2")
        self.a4 = QtWidgets.QLabel(self.centralwidget)
        self.a4.setGeometry(QtCore.QRect(625, 325, 75, 75))
        self.a4.setText("")
        self.a4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.a4.setObjectName("a4")
        self.b3 = QtWidgets.QLabel(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(550, 250, 75, 75))
        self.b3.setText("")
        self.b3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.b3.setObjectName("b3")
        self.e3 = QtWidgets.QLabel(self.centralwidget)
        self.e3.setGeometry(QtCore.QRect(325, 250, 75, 75))
        self.e3.setText("")
        self.e3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.e3.setObjectName("e3")
        self.b4 = QtWidgets.QLabel(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(550, 325, 75, 75))
        self.b4.setText("")
        self.b4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.b4.setObjectName("b4")
        self.c7 = QtWidgets.QLabel(self.centralwidget)
        self.c7.setGeometry(QtCore.QRect(475, 550, 75, 75))
        self.c7.setText("")
        self.c7.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.c7.setObjectName("c7")
        self.b7 = QtWidgets.QLabel(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(550, 550, 75, 75))
        self.b7.setText("")
        self.b7.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.b7.setObjectName("b7")
        self.f6 = QtWidgets.QLabel(self.centralwidget)
        self.f6.setGeometry(QtCore.QRect(250, 475, 75, 75))
        self.f6.setText("")
        self.f6.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.f6.setObjectName("f6")
        self.f7 = QtWidgets.QLabel(self.centralwidget)
        self.f7.setGeometry(QtCore.QRect(250, 550, 75, 75))
        self.f7.setText("")
        self.f7.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.f7.setObjectName("f7")
        self.c2 = QtWidgets.QLabel(self.centralwidget)
        self.c2.setGeometry(QtCore.QRect(475, 175, 75, 75))
        self.c2.setText("")
        self.c2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.c2.setObjectName("c2")
        self.f3 = QtWidgets.QLabel(self.centralwidget)
        self.f3.setGeometry(QtCore.QRect(250, 250, 75, 75))
        self.f3.setText("")
        self.f3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.f3.setObjectName("f3")
        self.e2 = QtWidgets.QLabel(self.centralwidget)
        self.e2.setGeometry(QtCore.QRect(325, 175, 75, 75))
        self.e2.setText("")
        self.e2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.e2.setObjectName("e2")
        self.h2 = QtWidgets.QLabel(self.centralwidget)
        self.h2.setGeometry(QtCore.QRect(100, 175, 75, 75))
        self.h2.setText("")
        self.h2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.h2.setObjectName("h2")
        self.b2 = QtWidgets.QLabel(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(550, 175, 75, 75))
        self.b2.setText("")
        self.b2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.b2.setObjectName("b2")
        self.a6 = QtWidgets.QLabel(self.centralwidget)
        self.a6.setGeometry(QtCore.QRect(625, 475, 75, 75))
        self.a6.setText("")
        self.a6.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.a6.setObjectName("a6")
        self.h4 = QtWidgets.QLabel(self.centralwidget)
        self.h4.setGeometry(QtCore.QRect(100, 325, 75, 75))
        self.h4.setText("")
        self.h4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.h4.setObjectName("h4")
        self.c6 = QtWidgets.QLabel(self.centralwidget)
        self.c6.setGeometry(QtCore.QRect(475, 475, 75, 75))
        self.c6.setText("")
        self.c6.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.c6.setObjectName("c6")
        self.e4 = QtWidgets.QLabel(self.centralwidget)
        self.e4.setGeometry(QtCore.QRect(325, 325, 75, 75))
        self.e4.setText("")
        self.e4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.e4.setObjectName("e4")
        self.d6 = QtWidgets.QLabel(self.centralwidget)
        self.d6.setGeometry(QtCore.QRect(400, 475, 75, 75))
        self.d6.setText("")
        self.d6.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.d6.setObjectName("d6")
        self.d3 = QtWidgets.QLabel(self.centralwidget)
        self.d3.setGeometry(QtCore.QRect(400, 250, 75, 75))
        self.d3.setText("")
        self.d3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.d3.setObjectName("d3")
        self.f8 = QtWidgets.QLabel(self.centralwidget)
        self.f8.setGeometry(QtCore.QRect(250, 625, 75, 75))
        self.f8.setText("")
        self.f8.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.f8.setObjectName("f8")
        self.d4 = QtWidgets.QLabel(self.centralwidget)
        self.d4.setGeometry(QtCore.QRect(400, 325, 75, 75))
        self.d4.setText("")
        self.d4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.d4.setObjectName("d4")
        self.c3 = QtWidgets.QLabel(self.centralwidget)
        self.c3.setGeometry(QtCore.QRect(475, 250, 75, 75))
        self.c3.setText("")
        self.c3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.c3.setObjectName("c3")
        self.e7 = QtWidgets.QLabel(self.centralwidget)
        self.e7.setGeometry(QtCore.QRect(325, 550, 75, 75))
        self.e7.setText("")
        self.e7.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.e7.setObjectName("e7")
        self.h8 = QtWidgets.QLabel(self.centralwidget)
        self.h8.setGeometry(QtCore.QRect(100, 625, 75, 75))
        self.h8.setText("")
        self.h8.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.h8.setObjectName("h8")
        self.h5 = QtWidgets.QLabel(self.centralwidget)
        self.h5.setGeometry(QtCore.QRect(100, 400, 75, 75))
        self.h5.setText("")
        self.h5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.h5.setObjectName("h5")
        self.a3 = QtWidgets.QLabel(self.centralwidget)
        self.a3.setGeometry(QtCore.QRect(625, 250, 75, 75))
        self.a3.setText("")
        self.a3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.a3.setObjectName("a3")
        self.b8 = QtWidgets.QLabel(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(550, 625, 75, 75))
        self.b8.setText("")
        self.b8.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.b8.setObjectName("b8")
        self.b5 = QtWidgets.QLabel(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(550, 400, 75, 75))
        self.b5.setText("")
        self.b5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.b5.setObjectName("b5")
        self.h7 = QtWidgets.QLabel(self.centralwidget)
        self.h7.setGeometry(QtCore.QRect(100, 550, 75, 75))
        self.h7.setText("")
        self.h7.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.h7.setObjectName("h7")
        self.d8 = QtWidgets.QLabel(self.centralwidget)
        self.d8.setGeometry(QtCore.QRect(400, 625, 75, 75))
        self.d8.setText("")
        self.d8.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.d8.setObjectName("d8")
        self.a5 = QtWidgets.QLabel(self.centralwidget)
        self.a5.setGeometry(QtCore.QRect(625, 400, 75, 75))
        self.a5.setText("")
        self.a5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.a5.setObjectName("a5")
        self.e6 = QtWidgets.QLabel(self.centralwidget)
        self.e6.setGeometry(QtCore.QRect(325, 475, 75, 75))
        self.e6.setText("")
        self.e6.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.e6.setObjectName("e6")
        self.f2 = QtWidgets.QLabel(self.centralwidget)
        self.f2.setGeometry(QtCore.QRect(250, 175, 75, 75))
        self.f2.setText("")
        self.f2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.f2.setObjectName("f2")
        self.g2 = QtWidgets.QLabel(self.centralwidget)
        self.g2.setGeometry(QtCore.QRect(175, 175, 75, 75))
        self.g2.setText("")
        self.g2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.g2.setObjectName("g2")
        self.h6 = QtWidgets.QLabel(self.centralwidget)
        self.h6.setGeometry(QtCore.QRect(100, 475, 75, 75))
        self.h6.setText("")
        self.h6.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.h6.setObjectName("h6")
        self.c8 = QtWidgets.QLabel(self.centralwidget)
        self.c8.setGeometry(QtCore.QRect(475, 625, 75, 75))
        self.c8.setText("")
        self.c8.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.c8.setObjectName("c8")
        self.g7 = QtWidgets.QLabel(self.centralwidget)
        self.g7.setGeometry(QtCore.QRect(175, 550, 75, 75))
        self.g7.setText("")
        self.g7.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.g7.setObjectName("g7")
        self.g8 = QtWidgets.QLabel(self.centralwidget)
        self.g8.setGeometry(QtCore.QRect(175, 625, 75, 75))
        self.g8.setText("")
        self.g8.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.g8.setObjectName("g8")
        self.e5 = QtWidgets.QLabel(self.centralwidget)
        self.e5.setGeometry(QtCore.QRect(325, 400, 75, 75))
        self.e5.setText("")
        self.e5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.e5.setObjectName("e5")
        self.g5 = QtWidgets.QLabel(self.centralwidget)
        self.g5.setGeometry(QtCore.QRect(175, 400, 75, 75))
        self.g5.setText("")
        self.g5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.g5.setObjectName("g5")
        self.e8 = QtWidgets.QLabel(self.centralwidget)
        self.e8.setGeometry(QtCore.QRect(325, 625, 75, 75))
        self.e8.setText("")
        self.e8.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.e8.setObjectName("e8")
        self.a8 = QtWidgets.QLabel(self.centralwidget)
        self.a8.setGeometry(QtCore.QRect(625, 625, 75, 75))
        self.a8.setText("")
        self.a8.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.a8.setObjectName("a8")
        self.d7 = QtWidgets.QLabel(self.centralwidget)
        self.d7.setGeometry(QtCore.QRect(400, 550, 75, 75))
        self.d7.setText("")
        self.d7.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.d7.setObjectName("d7")
        self.f4 = QtWidgets.QLabel(self.centralwidget)
        self.f4.setGeometry(QtCore.QRect(250, 325, 75, 75))
        self.f4.setText("")
        self.f4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.f4.setObjectName("f4")
        self.d2 = QtWidgets.QLabel(self.centralwidget)
        self.d2.setGeometry(QtCore.QRect(400, 175, 75, 75))
        self.d2.setText("")
        self.d2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.d2.setObjectName("d2")
        self.g3 = QtWidgets.QLabel(self.centralwidget)
        self.g3.setGeometry(QtCore.QRect(175, 250, 75, 75))
        self.g3.setText("")
        self.g3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.g3.setObjectName("g3")
        self.h3 = QtWidgets.QLabel(self.centralwidget)
        self.h3.setGeometry(QtCore.QRect(100, 250, 75, 75))
        self.h3.setText("")
        self.h3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.h3.setObjectName("h3")
        self.box_1 = QtWidgets.QLabel(self.centralwidget)
        self.box_1.setGeometry(QtCore.QRect(830, 470, 75, 75))
        self.box_1.setMinimumSize(QtCore.QSize(71, 75))
        self.box_1.setText("")
        self.box_1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_1.setObjectName("box_1")
        self.box_2 = QtWidgets.QLabel(self.centralwidget)
        self.box_2.setGeometry(QtCore.QRect(910, 400, 75, 75))
        self.box_2.setMinimumSize(QtCore.QSize(71, 75))
        self.box_2.setText("")
        self.box_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_2.setObjectName("box_2")
        self.box_3 = QtWidgets.QLabel(self.centralwidget)
        self.box_3.setGeometry(QtCore.QRect(920, 500, 75, 75))
        self.box_3.setMinimumSize(QtCore.QSize(71, 75))
        self.box_3.setText("")
        self.box_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_3.setObjectName("box_3")
        self.box_4 = QtWidgets.QLabel(self.centralwidget)
        self.box_4.setGeometry(QtCore.QRect(1020, 470, 75, 75))
        self.box_4.setMinimumSize(QtCore.QSize(71, 75))
        self.box_4.setText("")
        self.box_4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_4.setObjectName("box_4")
        self.box_5 = QtWidgets.QLabel(self.centralwidget)
        self.box_5.setGeometry(QtCore.QRect(1020, 570, 75, 75))
        self.box_5.setMinimumSize(QtCore.QSize(71, 75))
        self.box_5.setText("")
        self.box_5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_5.setObjectName("box_5")
        self.box_6 = QtWidgets.QLabel(self.centralwidget)
        self.box_6.setGeometry(QtCore.QRect(930, 610, 75, 75))
        self.box_6.setMinimumSize(QtCore.QSize(71, 75))
        self.box_6.setText("")
        self.box_6.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_6.setObjectName("box_6")
        self.box_7 = QtWidgets.QLabel(self.centralwidget)
        self.box_7.setGeometry(QtCore.QRect(830, 580, 75, 75))
        self.box_7.setMinimumSize(QtCore.QSize(71, 75))
        self.box_7.setText("")
        self.box_7.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_7.setObjectName("box_7")
        self.box_8 = QtWidgets.QLabel(self.centralwidget)
        self.box_8.setGeometry(QtCore.QRect(1110, 600, 75, 75))
        self.box_8.setMinimumSize(QtCore.QSize(71, 75))
        self.box_8.setText("")
        self.box_8.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_8.setObjectName("box_8")
        self.box_9 = QtWidgets.QLabel(self.centralwidget)
        self.box_9.setGeometry(QtCore.QRect(1120, 490, 75, 75))
        self.box_9.setMinimumSize(QtCore.QSize(71, 75))
        self.box_9.setText("")
        self.box_9.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_9.setObjectName("box_9")
        self.box_10 = QtWidgets.QLabel(self.centralwidget)
        self.box_10.setGeometry(QtCore.QRect(1010, 380, 75, 75))
        self.box_10.setMinimumSize(QtCore.QSize(71, 75))
        self.box_10.setText("")
        self.box_10.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_10.setObjectName("box_10")
        self.box_11 = QtWidgets.QLabel(self.centralwidget)
        self.box_11.setGeometry(QtCore.QRect(750, 510, 75, 75))
        self.box_11.setMinimumSize(QtCore.QSize(71, 75))
        self.box_11.setText("")
        self.box_11.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_11.setObjectName("box_11")
        self.box_12 = QtWidgets.QLabel(self.centralwidget)
        self.box_12.setGeometry(QtCore.QRect(1100, 370, 75, 75))
        self.box_12.setMinimumSize(QtCore.QSize(71, 75))
        self.box_12.setText("")
        self.box_12.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_12.setObjectName("box_12")
        self.box_13 = QtWidgets.QLabel(self.centralwidget)
        self.box_13.setGeometry(QtCore.QRect(840, 150, 75, 75))
        self.box_13.setMinimumSize(QtCore.QSize(71, 75))
        self.box_13.setText("")
        self.box_13.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_13.setObjectName("box_13")
        self.box_14 = QtWidgets.QLabel(self.centralwidget)
        self.box_14.setGeometry(QtCore.QRect(990, 230, 75, 75))
        self.box_14.setMinimumSize(QtCore.QSize(71, 75))
        self.box_14.setText("")
        self.box_14.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_14.setObjectName("box_14")
        self.box_15 = QtWidgets.QLabel(self.centralwidget)
        self.box_15.setGeometry(QtCore.QRect(800, 50, 75, 75))
        self.box_15.setMinimumSize(QtCore.QSize(71, 75))
        self.box_15.setText("")
        self.box_15.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_15.setObjectName("box_15")
        self.box_16 = QtWidgets.QLabel(self.centralwidget)
        self.box_16.setGeometry(QtCore.QRect(1020, 30, 75, 75))
        self.box_16.setMinimumSize(QtCore.QSize(71, 75))
        self.box_16.setText("")
        self.box_16.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_16.setObjectName("box_16")
        self.box_17 = QtWidgets.QLabel(self.centralwidget)
        self.box_17.setGeometry(QtCore.QRect(1040, 120, 75, 75))
        self.box_17.setMinimumSize(QtCore.QSize(71, 75))
        self.box_17.setText("")
        self.box_17.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_17.setObjectName("box_17")
        self.box_18 = QtWidgets.QLabel(self.centralwidget)
        self.box_18.setGeometry(QtCore.QRect(750, 160, 75, 75))
        self.box_18.setMinimumSize(QtCore.QSize(71, 75))
        self.box_18.setText("")
        self.box_18.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_18.setObjectName("box_18")
        self.box_19 = QtWidgets.QLabel(self.centralwidget)
        self.box_19.setGeometry(QtCore.QRect(930, 150, 75, 75))
        self.box_19.setMinimumSize(QtCore.QSize(71, 75))
        self.box_19.setText("")
        self.box_19.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_19.setObjectName("box_19")
        self.box_20 = QtWidgets.QLabel(self.centralwidget)
        self.box_20.setGeometry(QtCore.QRect(920, 50, 75, 75))
        self.box_20.setMinimumSize(QtCore.QSize(71, 75))
        self.box_20.setText("")
        self.box_20.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_20.setObjectName("box_20")
        self.box_21 = QtWidgets.QLabel(self.centralwidget)
        self.box_21.setGeometry(QtCore.QRect(1150, 110, 75, 75))
        self.box_21.setMinimumSize(QtCore.QSize(71, 75))
        self.box_21.setText("")
        self.box_21.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_21.setObjectName("box_21")
        self.box_22 = QtWidgets.QLabel(self.centralwidget)
        self.box_22.setGeometry(QtCore.QRect(1090, 210, 75, 75))
        self.box_22.setMinimumSize(QtCore.QSize(71, 75))
        self.box_22.setText("")
        self.box_22.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_22.setObjectName("box_22")
        self.box_23 = QtWidgets.QLabel(self.centralwidget)
        self.box_23.setGeometry(QtCore.QRect(1110, 20, 75, 75))
        self.box_23.setMinimumSize(QtCore.QSize(71, 75))
        self.box_23.setText("")
        self.box_23.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_23.setObjectName("box_23")
        self.box_24 = QtWidgets.QLabel(self.centralwidget)
        self.box_24.setGeometry(QtCore.QRect(880, 250, 75, 75))
        self.box_24.setMinimumSize(QtCore.QSize(71, 75))
        self.box_24.setText("")
        self.box_24.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.box_24.setObjectName("box_24")
        self.step = QtWidgets.QLabel(self.centralwidget)
        self.step.setGeometry(QtCore.QRect(390, 10, 75, 75))
        self.step.setMinimumSize(QtCore.QSize(71, 75))
        self.step.setText("")
        self.step.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.step.setObjectName("step")
        self.step_2 = QtWidgets.QLabel(self.centralwidget)
        self.step_2.setGeometry(QtCore.QRect(280, 10, 111, 75))
        self.step_2.setMinimumSize(QtCore.QSize(71, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.step_2.setFont(font)
        self.step_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.step_2.setObjectName("step_2")
        self.giveupButton = QtWidgets.QPushButton(self.centralwidget)
        self.giveupButton.setGeometry(QtCore.QRect(1210, 730, 80, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.giveupButton.setFont(font)
        self.giveupButton.setObjectName("giveupButton")
        self.win_label = QtWidgets.QLabel(self.centralwidget)
        self.win_label.setGeometry(QtCore.QRect(350, 225, 600, 350))
        self.win_label.setText("")
        self.win_label.setObjectName("win_label")
        self.play_again_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_again_button.setGeometry(QtCore.QRect(600, 500, 100, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.play_again_button.setFont(font)
        self.play_again_button.setObjectName("play_again_button")
        self.boardLabel.raise_()
        self.e1.raise_()
        self.b1.raise_()
        self.a7.raise_()
        self.b6.raise_()
        self.c5.raise_()
        self.d5.raise_()
        self.c4.raise_()
        self.f5.raise_()
        self.g1.raise_()
        self.g6.raise_()
        self.a1.raise_()
        self.g4.raise_()
        self.a2.raise_()
        self.a4.raise_()
        self.b3.raise_()
        self.e3.raise_()
        self.b4.raise_()
        self.c7.raise_()
        self.b7.raise_()
        self.f6.raise_()
        self.f7.raise_()
        self.c2.raise_()
        self.f3.raise_()
        self.e2.raise_()
        self.d1.raise_()
        self.h2.raise_()
        self.b2.raise_()
        self.a6.raise_()
        self.h4.raise_()
        self.c6.raise_()
        self.e4.raise_()
        self.d6.raise_()
        self.d3.raise_()
        self.f8.raise_()
        self.h1.raise_()
        self.d4.raise_()
        self.c3.raise_()
        self.e7.raise_()
        self.h8.raise_()
        self.h5.raise_()
        self.a3.raise_()
        self.b8.raise_()
        self.f1.raise_()
        self.b5.raise_()
        self.h7.raise_()
        self.d8.raise_()
        self.a5.raise_()
        self.c1.raise_()
        self.e6.raise_()
        self.f2.raise_()
        self.g2.raise_()
        self.h6.raise_()
        self.c8.raise_()
        self.g7.raise_()
        self.g8.raise_()
        self.e5.raise_()
        self.g5.raise_()
        self.e8.raise_()
        self.a8.raise_()
        self.d7.raise_()
        self.f4.raise_()
        self.d2.raise_()
        self.g3.raise_()
        self.h3.raise_()
        self.box_1.raise_()
        self.box_2.raise_()
        self.box_3.raise_()
        self.box_4.raise_()
        self.box_5.raise_()
        self.box_6.raise_()
        self.box_7.raise_()
        self.box_8.raise_()
        self.box_9.raise_()
        self.box_10.raise_()
        self.box_11.raise_()
        self.box_12.raise_()
        self.box_13.raise_()
        self.box_14.raise_()
        self.box_15.raise_()
        self.box_16.raise_()
        self.box_17.raise_()
        self.box_18.raise_()
        self.box_19.raise_()
        self.box_20.raise_()
        self.box_21.raise_()
        self.box_22.raise_()
        self.box_23.raise_()
        self.box_24.raise_()
        self.step.raise_()
        self.step_2.raise_()
        self.giveupButton.raise_()
        self.win_label.raise_()
        self.play_again_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "??????????"))
        self.step_2.setText(_translate("MainWindow", "?????????? -"))
        self.giveupButton.setText(_translate("MainWindow", "????????????"))
        self.play_again_button.setText(_translate("MainWindow", "???????????? ????????????"))
