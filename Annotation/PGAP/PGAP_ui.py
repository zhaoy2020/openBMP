# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/openBMP/PGAP.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PGAP(object):
    def setupUi(self, PGAP):
        PGAP.setObjectName("PGAP")
        PGAP.resize(339, 541)
        self.centralwidget = QtWidgets.QWidget(PGAP)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 2, 1, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox_10 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout_3.addWidget(self.checkBox_10, 0, 0, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_3.addWidget(self.checkBox_7, 0, 1, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_3.addWidget(self.checkBox_9, 1, 0, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout_3.addWidget(self.checkBox_11, 1, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_3.addWidget(self.checkBox_3, 2, 0, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_3.addWidget(self.checkBox_8, 2, 1, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_3.addWidget(self.checkBox_4, 3, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_3.addWidget(self.checkBox_5, 3, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_3.addWidget(self.checkBox_6, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 4, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_4.addWidget(self.checkBox)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_4.addWidget(self.checkBox_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_3.addWidget(self.frame)
        PGAP.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PGAP)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 339, 17))
        self.menubar.setObjectName("menubar")
        PGAP.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PGAP)
        self.statusbar.setObjectName("statusbar")
        PGAP.setStatusBar(self.statusbar)

        self.retranslateUi(PGAP)
        QtCore.QMetaObject.connectSlotsByName(PGAP)

    def retranslateUi(self, PGAP):
        _translate = QtCore.QCoreApplication.translate
        PGAP.setWindowTitle(_translate("PGAP", "NCBI Prokaryotic Genome Annotation Pipeline"))
        self.groupBox.setTitle(_translate("PGAP", "Work station"))
        self.label.setText(_translate("PGAP", "Genome sequence (fna)"))
        self.pushButton.setText(_translate("PGAP", "Open dir."))
        self.groupBox_2.setTitle(_translate("PGAP", "Configure"))
        self.groupBox_4.setTitle(_translate("PGAP", "Input.yaml"))
        self.label_2.setText(_translate("PGAP", "class"))
        self.lineEdit_2.setText(_translate("PGAP", "File"))
        self.label_3.setText(_translate("PGAP", "location"))
        self.lineEdit_3.setText(_translate("PGAP", "File"))
        self.groupBox_5.setTitle(_translate("PGAP", "Sumbol.yaml"))
        self.label_4.setText(_translate("PGAP", "genus_species"))
        self.lineEdit_5.setText(_translate("PGAP", "Brevundimonas naejangsanensis"))
        self.label_5.setText(_translate("PGAP", "strain"))
        self.lineEdit_4.setText(_translate("PGAP", "ML17"))
        self.label_6.setText(_translate("PGAP", "topology"))
        self.lineEdit_6.setText(_translate("PGAP", "circular"))
        self.pushButton_4.setText(_translate("PGAP", "Load configure"))
        self.pushButton_5.setText(_translate("PGAP", "Save configure"))
        self.groupBox_6.setTitle(_translate("PGAP", "Parameter"))
        self.checkBox_10.setText(_translate("PGAP", "ignore-all-errors"))
        self.checkBox_7.setText(_translate("PGAP", "no-internet"))
        self.checkBox_9.setText(_translate("PGAP", "update"))
        self.checkBox_11.setText(_translate("PGAP", "no-self-update"))
        self.checkBox_3.setText(_translate("PGAP", "report-usage-false"))
        self.checkBox_8.setText(_translate("PGAP", "report-usage-true"))
        self.checkBox_4.setText(_translate("PGAP", "taxcheck"))
        self.checkBox_5.setText(_translate("PGAP", "taxcheck-only"))
        self.checkBox_6.setText(_translate("PGAP", "auto-correct-tax"))
        self.label_7.setText(_translate("PGAP", "requires taxcheck"))
        self.groupBox_3.setTitle(_translate("PGAP", "Script"))
        self.pushButton_2.setText(_translate("PGAP", "Generate bash script"))
        self.checkBox.setText(_translate("PGAP", "remote"))
        self.checkBox_2.setText(_translate("PGAP", "local"))
        self.pushButton_3.setText(_translate("PGAP", "Start PGAP"))
