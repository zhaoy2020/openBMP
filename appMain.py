# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:22:42 2023

@author: zhao
"""

import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui 
'''
PyQt5:
    QtWidgets:
        QApplication            # 应用程序
        QWidget                 # 窗体
        QDialog                 # 窗体
        QMainWindow             # 窗体
        QLabel
        QFileDialog             # 对话框
        QMessageBox             # 消息框
    QtCore:
        pyqtSignal              # 信号函数
        pyqtSlot                # 槽函数
        Qt                      # 菜单控件
        QObject
    QtGui
'''


import Main.OpenBMP_logic as OpenBMP_logic
print(f'注意这是{__name__}整个程序的入口位置：{os.getcwd()}')   # 很重要



if __name__ == "__main__":
    '''
    appMain创建应用程序和窗体，然后显示窗体，并开始运行应用程序；
    将ui.py文件的测试运行部分单独拿出来作为一个文件。
    当一个应用程序有多个窗体，并且窗体之间有数据传输时，
    appMain.py负责创建应用程序的主窗体并运行起来，
    这样整个应用程序的结构就更加清晰了。
    '''
    app = QtWidgets.QApplication(sys.argv)  # 第一步创建GUI应用程序，固定步骤

    window = OpenBMP_logic.QmyMianWindow()  # 第二步在应用上创建主窗口
    window.show()                           # 显示主窗口所有内容
    
    sys.exit(app.exec_())                   # 执行应用循环，固定步骤
