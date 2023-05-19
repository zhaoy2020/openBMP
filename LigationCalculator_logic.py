# -*- coding: utf-8 -*-
"""
Created on Fri May 19 15:19:33 2023

@author: zhao
"""

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
'''
PyQt5:
    QtWidgets:
        QApplication
        QWidget
        QDialog
        QMainWindow
        QLabel
        QFileDialog
    QtCore:
        pyqtSignal
        pyqtSlot
        Qt
        QObject
    QtGui
'''

import LigationCalculator_ui  # 导入ui.py创建的类


class QLigationCalculator(QtWidgets.QDialog):
    '''
    LocalBlastGUI逻辑部分
    '''
    def __init__(self, parent=None):
        
        super().__init__(parent) # 继承QtWidgets.QDialog
        self.ui = LigationCalculator_ui.Ui_LigationCalculator()
        self.ui.setupUi(self)

##  ===============================有connectSlotsByName()自动关联的槽函数===============================
    def reactionVolume(self, FOLD, M1, C1, M2, C2, v2, VOLUE):
        FOLD = float(FOLD)
        M1 = float(M1)
        C1 = float(C1)
        M2 = float(M2)
        C2 = float(C2)
        v2 = float(v2)
        VOLUE = float(VOLUE)
        K = (FOLD * M1 * C2)/(M2 * C1)
        v1 = K * v2
        vH2O = VOLUE - v1 - v2
        return [str(v1), str(v2), str(vH2O), str((C1*v1 + C2*v2))]
        
    @QtCore.pyqtSlot()
    def on_pushButton_5_clicked(self):
        try:
            M1 = self.ui.lineEdit.text()
            C1 = self.ui.lineEdit_2.text()
            M2 = self.ui.lineEdit_5.text()
            C2 = self.ui.lineEdit_4.text()
            v2 = self.ui.lineEdit_7.text()
            VOLUE = self.ui.lineEdit_6.text()
            
            self.ui.label_15.setText(self.reactionVolume(1, M1, C1, M2, C2, v2, VOLUE)[0])
            self.ui.label_14.setText(self.reactionVolume(1, M1, C1, M2, C2, v2, VOLUE)[1])
            self.ui.label_13.setText(self.reactionVolume(1, M1, C1, M2, C2, v2, VOLUE)[2])
            self.ui.label_4.setText(self.reactionVolume(1, M1, C1, M2, C2, v2, VOLUE)[3])
            
            self.ui.label_18.setText(self.reactionVolume(2, M1, C1, M2, C2, v2, VOLUE)[0])
            self.ui.label_19.setText(self.reactionVolume(2, M1, C1, M2, C2, v2, VOLUE)[1])
            self.ui.label_17.setText(self.reactionVolume(2, M1, C1, M2, C2, v2, VOLUE)[2])
            self.ui.label_9.setText(self.reactionVolume(2, M1, C1, M2, C2, v2, VOLUE)[3])
            
            self.ui.label_23.setText(self.reactionVolume(3, M1, C1, M2, C2, v2, VOLUE)[0])
            self.ui.label_24.setText(self.reactionVolume(3, M1, C1, M2, C2, v2, VOLUE)[1])
            self.ui.label_21.setText(self.reactionVolume(3, M1, C1, M2, C2, v2, VOLUE)[2])
            self.ui.label_34.setText(self.reactionVolume(3, M1, C1, M2, C2, v2, VOLUE)[3])
            
            self.ui.label_27.setText(self.reactionVolume(5, M1, C1, M2, C2, v2, VOLUE)[0])
            self.ui.label_26.setText(self.reactionVolume(5, M1, C1, M2, C2, v2, VOLUE)[1])
            self.ui.label_28.setText(self.reactionVolume(5, M1, C1, M2, C2, v2, VOLUE)[2])
            self.ui.label_35.setText(self.reactionVolume(5, M1, C1, M2, C2, v2, VOLUE)[3])
            
            self.ui.label_31.setText(self.reactionVolume(7, M1, C1, M2, C2, v2, VOLUE)[0])
            self.ui.label_32.setText(self.reactionVolume(7, M1, C1, M2, C2, v2, VOLUE)[1])
            self.ui.label_29.setText(self.reactionVolume(7, M1, C1, M2, C2, v2, VOLUE)[2])
            self.ui.label_36.setText(self.reactionVolume(7, M1, C1, M2, C2, v2, VOLUE)[3])
        except:
            QtWidgets.QMessageBox.warning(self, "错误", "不能为空！")
                


if __name__ == "__main__":
    '''
    appMain创建应用程序和窗体，然后显示窗体，并开始运行应用程序；
    将ui.py文件的测试运行部分单独拿出来作为一个文件。
    当一个应用程序有多个窗体，并且窗体之间有数据传输时，
    appMain.py负责创建应用程序的主窗体并运行起来，
    这样整个应用程序的结构就更加清晰了。
    '''
    app = QtWidgets.QApplication(sys.argv)  # 第一步创建GUI应用程序，固定步骤

    window = QLigationCalculator()  # 第二步在应用上创建主窗口
    window.show()  # 显示主窗口所有内容

    sys.exit(app.exec_())  # 执行应用循环，固定步骤