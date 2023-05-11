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

if False:
    # ====================================先将resource相关文件进行编译=======================================
    # =============================================================================
    # 编译resuource文件至py
    # =============================================================================
    resName = 'picture'
    rescmd = f"D:\ProgramFiles\miniconda3\Scripts\pyrcc5.exe UI/openBMP/{resName}.qrc -o {resName}_rc.py"
    os.system(rescmd)
    
    # =============================================================================
    # 编译openBMP.ui至py文件
    # =============================================================================
    uiName = "OpenBMP"
    # 放在UI文件夹下面
    uicmd = f'D:\ProgramFiles\miniconda3\python -m PyQt5.uic.pyuic UI/openBMP/{uiName}.ui -o {uiName}_ui.py'
    os.system(uicmd)  # 先将UI文件转格式为py格式文件
    
    # =============================================================================
    # 编译LocalBlastGUI.ui至py文件
    # =============================================================================
    uiName = "LocalBlastGUI"
    # 放在UI文件夹下面
    uicmd = f'D:\ProgramFiles\miniconda3\python -m PyQt5.uic.pyuic UI/openBMP/{uiName}.ui -o {uiName}_ui.py'
    os.system(uicmd)  # 先将UI文件转格式为py格式文件

import OpenBMP_logic



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
    window.show()  # 显示主窗口所有内容
    
    sys.exit(app.exec_())  # 执行应用循环，固定步骤
