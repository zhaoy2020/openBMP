# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/openBMP/LocalBlastGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LocalBlastGUI(object):
    def setupUi(self, LocalBlastGUI):
        LocalBlastGUI.setObjectName("LocalBlastGUI")
        LocalBlastGUI.resize(285, 461)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        LocalBlastGUI.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(LocalBlastGUI)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(LocalBlastGUI)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setDragEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setDragEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(LocalBlastGUI)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 0, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(LocalBlastGUI)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_2.setObjectName("spinBox_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox_2)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_3.setObjectName("spinBox_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBox_3)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_4.setAccelerated(False)
        self.doubleSpinBox_4.setDecimals(6)
        self.doubleSpinBox_4.setMinimum(1e-06)
        self.doubleSpinBox_4.setSingleStep(1e-05)
        self.doubleSpinBox_4.setProperty("value", 1e-05)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_4)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.spinBox_5 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_5.setObjectName("spinBox_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spinBox_5)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(LocalBlastGUI)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_4)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.retranslateUi(LocalBlastGUI)
        QtCore.QMetaObject.connectSlotsByName(LocalBlastGUI)

    def retranslateUi(self, LocalBlastGUI):
        _translate = QtCore.QCoreApplication.translate
        LocalBlastGUI.setWindowTitle(_translate("LocalBlastGUI", "Local Blast GUI"))
        self.groupBox.setTitle(_translate("LocalBlastGUI", "Work station"))
        self.label.setText(_translate("LocalBlastGUI", "DB path"))
        self.pushButton.setText(_translate("LocalBlastGUI", "File"))
        self.label_2.setText(_translate("LocalBlastGUI", "Query path"))
        self.pushButton_2.setText(_translate("LocalBlastGUI", "File"))
        self.label_3.setText(_translate("LocalBlastGUI", "Output path"))
        self.pushButton_3.setText(_translate("LocalBlastGUI", "Dir."))
        self.groupBox_2.setTitle(_translate("LocalBlastGUI", "Command"))
        self.pushButton_4.setText(_translate("LocalBlastGUI", "Format DB"))
        self.pushButton_5.setText(_translate("LocalBlastGUI", "Blast"))
        self.pushButton_6.setText(_translate("LocalBlastGUI", "Default parameters"))
        self.groupBox_3.setTitle(_translate("LocalBlastGUI", "Parameters"))
        self.label_4.setText(_translate("LocalBlastGUI", "dbtype"))
        self.comboBox.setCurrentText(_translate("LocalBlastGUI", "prot"))
        self.comboBox.setItemText(0, _translate("LocalBlastGUI", "prot"))
        self.comboBox.setItemText(1, _translate("LocalBlastGUI", "nucl"))
        self.label_5.setText(_translate("LocalBlastGUI", "CPU threads"))
        self.spinBox.setSpecialValueText(_translate("LocalBlastGUI", "2"))
        self.label_6.setText(_translate("LocalBlastGUI", "max_hsps"))
        self.spinBox_2.setSpecialValueText(_translate("LocalBlastGUI", "1"))
        self.label_7.setText(_translate("LocalBlastGUI", "num_aligments"))
        self.spinBox_3.setSpecialValueText(_translate("LocalBlastGUI", "1"))
        self.doubleSpinBox_4.setSpecialValueText(_translate("LocalBlastGUI", "0.00001"))
        self.label_9.setText(_translate("LocalBlastGUI", "outfmt"))
        self.spinBox_5.setSpecialValueText(_translate("LocalBlastGUI", "6"))
        self.label_10.setText(_translate("LocalBlastGUI", "Blasttype"))
        self.comboBox_2.setItemText(0, _translate("LocalBlastGUI", "blastp (aa/aa)"))
        self.comboBox_2.setItemText(1, _translate("LocalBlastGUI", "blastn (nt/nt)"))
        self.comboBox_2.setItemText(2, _translate("LocalBlastGUI", "blastx (nt/aa)"))
        self.comboBox_2.setItemText(3, _translate("LocalBlastGUI", "tblastn (aa/nt)"))
        self.label_8.setText(_translate("LocalBlastGUI", "Evalue"))
        self.groupBox_4.setTitle(_translate("LocalBlastGUI", "Termininal"))
