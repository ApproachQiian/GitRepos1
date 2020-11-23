# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'truly.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1236, 812)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, 35, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.imageWindow = PlotWidget(self.centralwidget)
        self.imageWindow.setEnabled(False)
        self.imageWindow.setStyleSheet("border:3px dashed #242424;")
        self.imageWindow.setObjectName("imageWindow")
        self.verticalLayout.addWidget(self.imageWindow)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_draw = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_draw.sizePolicy().hasHeightForWidth())
        self.btn_draw.setSizePolicy(sizePolicy)
        self.btn_draw.setStyleSheet(".QPushButton {\n"
"    box-shadow:inset 0px 1px 0px 0px #f5978e;\n"
"    background:linear-gradient(to bottom, #f24537 5%, #c62d1f 100%);\n"
"    background-color:#f24537;\n"
"    border-radius:6px;\n"
"    border:1px solid #d02718;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Arial;\n"
"    font-size:15px;\n"
"    font-weight:bold;\n"
"    padding:6px 24px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px 1px 0px #810e05;\n"
"}\n"
".QPushButton:hover {\n"
"    background:linear-gradient(to bottom, #c62d1f 5%, #f24537 100%);\n"
"    background-color:#c62d1f;\n"
"}\n"
".QPushButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"}")
        self.btn_draw.setObjectName("btn_draw")
        self.horizontalLayout_5.addWidget(self.btn_draw)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox {\n"
"     border :  1px  solid  gray ;\n"
"     border-radius:  3px ;\n"
"     padding :  1px  2px  1px  2px ;  \n"
"     min-width :  9em ;  \n"
"     text-align:center;\n"
"}\n"
"QComboBox:hover {\n"
"    background-color:rgb(230,230,230);\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet(".QPushButton {\n"
"    box-shadow:inset 0px 1px 0px 0px #bee2f9;\n"
"    background:linear-gradient(to bottom, #63b8ee 5%, #468ccf 100%);\n"
"    background-color:#63b8ee;\n"
"    border-radius:6px;\n"
"    border:1px solid #3866a3;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#14396a;\n"
"    font-family:Arial;\n"
"    font-size:15px;\n"
"    font-weight:bold;\n"
"    padding:6px 24px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px 1px 0px #7cacde;\n"
"}\n"
".QPushButton:hover {\n"
"    background:linear-gradient(to bottom, #468ccf 5%, #63b8ee 100%);\n"
"    background-color:#468ccf;\n"
"}\n"
".QPushButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"}")
        self.btn_save.setObjectName("btn_save")
        self.verticalLayout_2.addWidget(self.btn_save)
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setStyleSheet(".QPushButton {\n"
"    box-shadow:inset 0px 1px 0px 0px #ffffff;\n"
"    background:linear-gradient(to bottom, #f9f9f9 5%, #e9e9e9 100%);\n"
"    background-color:#f9f9f9;\n"
"    border-radius:6px;\n"
"    border:1px solid #dcdcdc;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#666666;\n"
"    font-family:Arial;\n"
"    font-size:15px;\n"
"    font-weight:bold;\n"
"    padding:6px 24px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px 1px 0px #ffffff;\n"
"}\n"
".QPushButton:hover {\n"
"    background:linear-gradient(to bottom, #e9e9e9 5%, #f9f9f9 100%);\n"
"    background-color:#e9e9e9;\n"
"}\n"
".QPushButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"}")
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout_2.addWidget(self.btn_exit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.treeView_2 = QtWidgets.QTreeView(self.centralwidget)
        self.treeView_2.setEnabled(False)
        self.treeView_2.setStyleSheet("background-image: url(\'C:/Users/85035/Desktop/backnew.png\');\n"
"background-repeat: no-repeat;\n"
"background-position:  center;\n"
"background-color:white;")
        self.treeView_2.setObjectName("treeView_2")
        self.horizontalLayout.addWidget(self.treeView_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(False)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_clean = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clean.sizePolicy().hasHeightForWidth())
        self.btn_clean.setSizePolicy(sizePolicy)
        self.btn_clean.setStyleSheet(".QPushButton {\n"
"    box-shadow:inset 0px 1px 0px 0px #bbdaf7;\n"
"    background:linear-gradient(to bottom, #79bbff 5%, #378de5 100%);\n"
"    background-color:#79bbff;\n"
"    border-radius:6px;\n"
"    border:1px solid #84bbf3;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Arial;\n"
"    font-size:15px;\n"
"    font-weight:bold;\n"
"    padding:6px 24px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px 1px 0px #528ecc;\n"
"}\n"
".QPushButton:hover {\n"
"    background:linear-gradient(to bottom, #378de5 5%, #79bbff 100%);\n"
"    background-color:#378de5;\n"
"}\n"
".QPushButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"}")
        self.btn_clean.setObjectName("btn_clean")
        self.horizontalLayout_2.addWidget(self.btn_clean)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1236, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Create Anime Characters With DCGAN!"))
        self.btn_draw.setText(_translate("MainWindow", "生成"))
        self.comboBox.setItemText(0, _translate("MainWindow", "二次元动漫图像"))
        self.btn_save.setText(_translate("MainWindow", "保存图片"))
        self.btn_exit.setText(_translate("MainWindow", "退出程序"))
        self.btn_clean.setText(_translate("MainWindow", "清除"))

from pyqtgraph import PlotWidget
