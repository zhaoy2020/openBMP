# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/openBMP/MarkPDF.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MarkPDF(object):
    def setupUi(self, MarkPDF):
        MarkPDF.setObjectName("MarkPDF")
        MarkPDF.resize(558, 304)
        MarkPDF.setMinimumSize(QtCore.QSize(0, 0))
        MarkPDF.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/bacteria.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MarkPDF.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MarkPDF)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_3.addWidget(self.frame)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        MarkPDF.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MarkPDF)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 17))
        self.menubar.setObjectName("menubar")
        MarkPDF.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MarkPDF)
        self.statusbar.setObjectName("statusbar")
        MarkPDF.setStatusBar(self.statusbar)

        self.retranslateUi(MarkPDF)
        QtCore.QMetaObject.connectSlotsByName(MarkPDF)

    def retranslateUi(self, MarkPDF):
        _translate = QtCore.QCoreApplication.translate
        MarkPDF.setWindowTitle(_translate("MarkPDF", "MarkPDF by Zhaoy"))
        self.groupBox.setTitle(_translate("MarkPDF", "Sci-Hub toolkit:"))
        self.textBrowser.setHtml(_translate("MarkPDF", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Download papers according to DOI/PMID/Title from sci-hub/PubMed websites.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Configure the location where to save the file and the associated configuration information, before performing a batch download.</span></p></body></html>"))
        self.pushButton_4.setText(_translate("MarkPDF", "Open sci-hub"))
        self.groupBox_2.setTitle(_translate("MarkPDF", "Batch hightlight key words within PDF:"))
        self.label_2.setText(_translate("MarkPDF", "RawPDF(Input):"))
        self.pushButton_3.setText(_translate("MarkPDF", "Choose dir."))
        self.lineEdit_3.setText(_translate("MarkPDF", "./MatchPDf"))
        self.label.setText(_translate("MarkPDF", "Query key words:"))
        self.lineEdit_2.setText(_translate("MarkPDF", "./RawPDF"))
        self.textEdit.setHtml(_translate("MarkPDF", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">cdG;cyclic di-GMP;c-diGMP;PDE;DGC</span></p></body></html>"))
        self.label_3.setText(_translate("MarkPDF", "MatchPDF(Output):"))
        self.pushButton.setText(_translate("MarkPDF", "Start"))
        self.pushButton_2.setText(_translate("MarkPDF", "Open dir."))