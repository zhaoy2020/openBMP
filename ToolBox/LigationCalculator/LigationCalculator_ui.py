# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/openBMP/LigationCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LigationCalculator(object):
    def setupUi(self, LigationCalculator):
        LigationCalculator.setObjectName("LigationCalculator")
        LigationCalculator.resize(538, 453)
        self.verticalLayout = QtWidgets.QVBoxLayout(LigationCalculator)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(LigationCalculator)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(LigationCalculator)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.comboBox_7.setFont(font)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_7, 0, 2, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 1, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_4, 1, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.groupBox_3)
        self.label_33.setObjectName("label_33")
        self.gridLayout_2.addWidget(self.label_33, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 2, 1, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.comboBox_6.setFont(font)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_6, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_11 = QtWidgets.QLabel(LigationCalculator)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.lineEdit_6 = QtWidgets.QLineEdit(LigationCalculator)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_4.addWidget(self.lineEdit_6)
        self.comboBox_5 = QtWidgets.QComboBox(LigationCalculator)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.comboBox_5.setFont(font)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_5 = QtWidgets.QPushButton(LigationCalculator)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(LigationCalculator)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_31 = QtWidgets.QLabel(self.groupBox)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout_3.addWidget(self.label_31, 5, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 4, 2, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.groupBox)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_3.addWidget(self.label_29, 5, 6, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 2, 4, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 4, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 5, 1, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.groupBox)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout_3.addWidget(self.label_36, 5, 7, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.groupBox)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout_3.addWidget(self.label_30, 5, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 3, 4, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 4, 6, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 3, 5, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.groupBox)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout_3.addWidget(self.label_34, 3, 7, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout_3.addWidget(self.label_26, 4, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 3, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 1, 5, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 1, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 3, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem10, 4, 5, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem11, 4, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(42, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem12, 1, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(42, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem13, 4, 3, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(42, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem14, 3, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 4, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 2, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 1, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 7, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem15, 2, 5, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(42, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem16, 0, 3, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(42, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem17, 2, 3, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem18, 5, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 7, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 1, 6, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem19, 0, 5, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(42, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem20, 5, 3, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 3, 6, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 7, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 6, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.groupBox)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout_3.addWidget(self.label_32, 5, 4, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 3, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 2, 6, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.groupBox)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_3.addWidget(self.label_35, 4, 7, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 2, 2, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem21, 2, 1, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.groupBox)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout_3.addWidget(self.label_37, 6, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.groupBox)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.gridLayout_3.addWidget(self.label_38, 6, 2, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.groupBox)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.gridLayout_3.addWidget(self.label_39, 6, 4, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.groupBox)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.gridLayout_3.addWidget(self.label_40, 6, 6, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.groupBox)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.gridLayout_3.addWidget(self.label_41, 6, 7, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem22, 6, 1, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem23, 6, 3, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem24, 6, 5, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(LigationCalculator)
        QtCore.QMetaObject.connectSlotsByName(LigationCalculator)

    def retranslateUi(self, LigationCalculator):
        _translate = QtCore.QCoreApplication.translate
        LigationCalculator.setWindowTitle(_translate("LigationCalculator", "Ligation Calculator"))
        self.groupBox_2.setTitle(_translate("LigationCalculator", "Insert DNA"))
        self.label_2.setText(_translate("LigationCalculator", "Insert DNA length"))
        self.comboBox_2.setItemText(0, _translate("LigationCalculator", "kb"))
        self.label_3.setText(_translate("LigationCalculator", "Concentration"))
        self.comboBox_3.setItemText(0, _translate("LigationCalculator", "ng/μL"))
        self.groupBox_3.setTitle(_translate("LigationCalculator", "Plasmid DNA"))
        self.comboBox_7.setItemText(0, _translate("LigationCalculator", "kb"))
        self.comboBox_4.setItemText(0, _translate("LigationCalculator", "ng/μL"))
        self.label_10.setText(_translate("LigationCalculator", "Concentration"))
        self.label_33.setText(_translate("LigationCalculator", "Add(V2)"))
        self.label_12.setText(_translate("LigationCalculator", "Vector DNA length"))
        self.comboBox_6.setItemText(0, _translate("LigationCalculator", "μL"))
        self.label_11.setText(_translate("LigationCalculator", "Total Volume(V1+V2+V3)"))
        self.comboBox_5.setItemText(0, _translate("LigationCalculator", "μL"))
        self.pushButton_5.setText(_translate("LigationCalculator", "Run"))
        self.groupBox.setTitle(_translate("LigationCalculator", "Solutions"))
        self.label_31.setText(_translate("LigationCalculator", "0"))
        self.label_27.setText(_translate("LigationCalculator", "0"))
        self.label_29.setText(_translate("LigationCalculator", "<html><head/><body><p>0</p></body></html>"))
        self.label_19.setText(_translate("LigationCalculator", "0"))
        self.label_25.setText(_translate("LigationCalculator", "5:1"))
        self.label_36.setText(_translate("LigationCalculator", "0"))
        self.label_30.setText(_translate("LigationCalculator", "7:1"))
        self.label_24.setText(_translate("LigationCalculator", "0"))
        self.label_28.setText(_translate("LigationCalculator", "<html><head/><body><p>0</p></body></html>"))
        self.label_34.setText(_translate("LigationCalculator", "0"))
        self.label_26.setText(_translate("LigationCalculator", "0"))
        self.label_23.setText(_translate("LigationCalculator", "0"))
        self.label_16.setText(_translate("LigationCalculator", "1:1"))
        self.label_5.setText(_translate("LigationCalculator", "Vector DNA volume(V2)"))
        self.label_20.setText(_translate("LigationCalculator", "2:1"))
        self.label_15.setText(_translate("LigationCalculator", "0"))
        self.label_14.setText(_translate("LigationCalculator", "0"))
        self.label_4.setText(_translate("LigationCalculator", "0"))
        self.label.setText(_translate("LigationCalculator", "Total(ng)"))
        self.label_13.setText(_translate("LigationCalculator", "<html><head/><body><p>0</p></body></html>"))
        self.label_21.setText(_translate("LigationCalculator", "<html><head/><body><p>0</p></body></html>"))
        self.label_9.setText(_translate("LigationCalculator", "0"))
        self.label_7.setText(_translate("LigationCalculator", "<html><head/><body><p>H<span style=\" vertical-align:sub;\">2</span>O volume(V3)</p></body></html>"))
        self.label_32.setText(_translate("LigationCalculator", "0"))
        self.label_22.setText(_translate("LigationCalculator", "3:1"))
        self.label_17.setText(_translate("LigationCalculator", "<html><head/><body><p>0</p></body></html>"))
        self.label_35.setText(_translate("LigationCalculator", "0"))
        self.label_8.setText(_translate("LigationCalculator", "Molar scale"))
        self.label_6.setText(_translate("LigationCalculator", "Insert DNA volume(V1)"))
        self.label_18.setText(_translate("LigationCalculator", "0"))
        self.label_37.setText(_translate("LigationCalculator", "8:1"))
        self.label_38.setText(_translate("LigationCalculator", "0"))
        self.label_39.setText(_translate("LigationCalculator", "0"))
        self.label_40.setText(_translate("LigationCalculator", "0"))
        self.label_41.setText(_translate("LigationCalculator", "0"))
