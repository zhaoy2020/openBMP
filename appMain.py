# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:22:42 2023

@author: zhao
"""
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
# PyQt5 (QtCore, QtGui, QtWidgets(QApplication, QWidget, QDialog, QMainWindow, QLabel...))

##====================================先将resource相关文件进行编译=======================================
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
import OpenBMP_ui  # 导入ui.py创建的类


# =============================================================================
# 编译LocalBlastGUI.ui至py文件
# =============================================================================
uiName = "LocalBlastGUI"
# 放在UI文件夹下面
uicmd = f'D:\ProgramFiles\miniconda3\python -m PyQt5.uic.pyuic UI/openBMP/{uiName}.ui -o {uiName}_ui.py'
os.system(uicmd)  # 先将UI文件转格式为py格式文件
import LocalBlastGUI_ui  # 导入ui.py创建的类



class QmyMianWindow(QtWidgets.QMainWindow):  # 使用单继承的方式进行操作
    '''
    主界面
    '''
    def __init__(self, parent=None):
        super().__init__(parent)  # 初始化QtWidgets.QMainWindow这个父类的__init__方法,此时self就变成了QtWidgets.QMainWindow这个父类了

        # self.setGeometry(0, 0, 1000, 500) # 调整坐标和窗口大小，更加灵活
        # self.resize(600,600) # 调整窗口大小，更加简便
        
        self.__ui = OpenBMP_ui.Ui_OpenBMP()  # 创建UI对象（实例化对象）
        self.__ui.setupUi(self)  # 构造UI，记得传self(QtWidgets.QMainWindow)
        
        self.__ui.label_2.setOpenExternalLinks(True) # 超链接至Github openBMP项目上


class QLocalBlastGUI(QtWidgets.QWidget):
    '''
    Local Blast GUI界面
    '''
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.__ui = LocalBlastGUI_ui.Ui_LocalBlastGUI()
        self.__ui.setupUi(self)


if __name__ == "__main__":
    '''
    appMain创建应用程序和窗体，然后显示窗体，并开始运行应用程序；
    将ui.py文件的测试运行部分单独拿出来作为一个文件。
    当一个应用程序有多个窗体，并且窗体之间有数据传输时，
    appMain.py负责创建应用程序的主窗体并运行起来，
    这样整个应用程序的结构就更加清晰了。
    '''
    app = QtWidgets.QApplication(sys.argv)  # 第一步创建GUI应用程序，固定步骤

    mainWindow = QmyMianWindow()  # 第二步在应用上创建主窗口
    mainWindow.show()  # 显示主窗口所有内容

    # localBlastGUI = QLocalBlastGUI()
    # localBlastGUI.show()
    
    sys.exit(app.exec_())  # 执行应用循环，固定步骤
