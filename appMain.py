# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:22:42 2023

@author: zhao
"""
# =============================================================================
# # import sys
# # sys.path.append("D:\\WorkStation\\PyhtonWorkStation\\20220410-comparative\\bmp")
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# # mpl.rcParams['pdf.fonttype'] = 42
# # plt.rc('font',family='Times New Roman')
# =============================================================================

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
# PyQt5 (QtCore, QtGui, QtWidgets(QApplication, QWidget, QDialog, QMainWindow, QLabel...))

# =============================================================================
# 将Qt设计的ui文件转格式为py个格式文件并作为module导入appMain中以便于被调用
# =============================================================================
uiName = "MainWindow"
# 放在UI文件夹下面
cmd = f'D:\ProgramFiles\miniconda3\python -m PyQt5.uic.pyuic UI/ColonyCounter/{uiName}.ui -o UI/ColonyCounter/{uiName}.py'
os.system(cmd)  # 先将UI文件转格式为py格式文件
import UI.ColonyCounter.MainWindow  # 导入ui.py创建的类


class QmyMianWindow(QtWidgets.QMainWindow):  # 使用单继承的方式进行操作
    def __init__(self, parent=None):
        super().__init__(parent)  # 初始化QtWidgets.QMainWindow这个父类的__init__方法,此时self就变成了QtWidgets.QMainWindow这个父类了

        self.ui = UI.ColonyCounter.MainWindow.Ui_MainWindow()  # 创建UI对象（实例化对象）
        self.ui.setupUi(self)  # 构造UI，记得穿self(QtWidgets.QMainWindow)


if __name__ == "__main__":
    '''
    appMain创建应用程序和窗体，然后显示窗体，并开始运行应用程序；
    将ui.py文件的测试运行部分单独拿出来作为一个文件。
    当一个应用程序有多个窗体，并且窗体之间有数据传输时，
    appMain.py负责创建应用程序的主窗体并运行起来，
    这样整个应用程序的结构就更加清晰了。
    '''
    app = QtWidgets.QApplication(sys.argv)  # 第一步创建GUI应用程序，固定步骤

    mainWindow = QmyMianWindow()  # 第二部在应用上创建主窗口
    mainWindow.show()  # 显示主窗口所有内容

    sys.exit(app.exec_())  # 执行应用循环，固定步骤
