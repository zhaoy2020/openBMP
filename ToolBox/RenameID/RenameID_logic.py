# -*- coding: utf-8 -*-
"""
Created on Mon May 22 14:29:31 2023

@author: zhao
"""

import os
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

# import RenameID_ui  # 导入ui.py创建的类
from ToolBox.RenameID import RenameID_ui


class QRenameID(QtWidgets.QDialog):
    '''
    LocalBlastGUI逻辑部分
    '''
    def __init__(self, parent=None):
        
        super().__init__(parent) # 继承QtWidgets.QWidget
        self.ui = RenameID_ui.Ui_RenameID()
        self.ui.setupUi(self)

##  ===============================有connectSlotsByName()自动关联的槽函数===============================
    @QtCore.pyqtSlot()
    def on_pushButton_clicked(self):
        '''
        m = c * v *mw
        '''
        try:
            pass
        except:
            QtWidgets.QMessageBox.warning(self, "错误", "不能为空！")
            
    @QtCore.pyqtSlot()
    def on_pushButton_2_clicked(self):
        pass

if __name__ == "__main__":
    '''
    appMain创建应用程序和窗体，然后显示窗体，并开始运行应用程序；
    将ui.py文件的测试运行部分单独拿出来作为一个文件。
    当一个应用程序有多个窗体，并且窗体之间有数据传输时，
    appMain.py负责创建应用程序的主窗体并运行起来，
    这样整个应用程序的结构就更加清晰了。
    '''
    app = QtWidgets.QApplication(sys.argv)  # 第一步创建GUI应用程序，固定步骤

    window = QRenameID()  # 第二步在应用上创建主窗口
    window.show()  # 显示主窗口所有内容

    sys.exit(app.exec_())  # 执行应用循环，固定步骤