# -*- coding: utf-8 -*-
"""
Created on Thu May 11 10:03:53 2023
负责主窗口OpenBMP的逻辑串联
@author: zhao
"""

import os
import sys
from PyQt5 import QtWidgets, QtCore
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
import LocalBlastGUI_logic
import LigationCalculator_logic

# =============================================================================
# 编译openBMP.ui至py文件
# =============================================================================
# uiName = "OpenBMP"
# # 放在UI文件夹下面
# uicmd = f'D:\ProgramFiles\miniconda3\python -m PyQt5.uic.pyuic UI/openBMP/{uiName}.ui -o {uiName}_ui.py'
# os.system(uicmd)  # 先将UI文件转格式为py格式文件
import OpenBMP_ui  # 导入ui.py创建的类


# =============================================================================
# 编写逻辑部分
# =============================================================================
class QmyMianWindow(QtWidgets.QMainWindow):  # 使用单继承的方式进行操作
    '''
    主界面
    '''
    def __init__(self, parent=None):
        super().__init__(parent)  # 初始化QtWidgets.QMainWindow这个父类的__init__方法,此时self就变成了QtWidgets.QMainWindow这个父类了
        self.ui = OpenBMP_ui.Ui_OpenBMP()  # 创建UI对象（实例化对象）
        self.ui.setupUi(self)  # 构造UI，记得传self(QtWidgets.QMainWindow)

        self.ui.label_2.setOpenExternalLinks(True)  # 超链接至Github openBMP项目上

##  ===============================有connectSlotsByName()自动关联的槽函数===============================
    @QtCore.pyqtSlot()
    def on_actionLocal_Blast_GUI_triggered(self):
        '''
        点击Local Blast GUI时候自动触发的槽函数
        创建一个LocalBlastGUI(QWidget)对象并添加到openBMP主界面的tabWidget的分页上
        '''
        print('单击Local Blast GUI')
        localBlastGUI = LocalBlastGUI_logic.QLocalBlastGUI(self)
        localBlastGUI.setAttribute(QtCore.Qt.WA_DeleteOnClose)  # 关闭时自动删除，很重要
        curIndex = self.ui.tabWidget.addTab(localBlastGUI, f"BlatGUI {self.ui.tabWidget.count()}")
        self.ui.tabWidget.setCurrentIndex(curIndex)

    def on_tabWidget_tabCloseRequested(self, index):
        '''
        分页关闭时关闭窗体
        自动关联的槽函数，否无法关闭tabWidget的窗口
        '''
        print(f"删除index为{index}的tabWidget窗口")
        self.ui.tabWidget.widget(index).close()
        
    @QtCore.pyqtSlot()
    def on_actionLigation_Calculator_triggered(self):
        LigationCalculator = LigationCalculator_logic.QLigationCalculator(self)
        LigationCalculator.show()


    @QtCore.pyqtSlot()
    def on_actionGomoku_triggered(self):
        print('This is a test.')
        try:
            os.popen(f'python ./Scripts/Gomoku.py')
        except:
            pass 

    @QtCore.pyqtSlot()
    def on_actionGreedy_Snake_triggered(self):
        print('This is a test.')
        try:
            os.popen(f'python ./Scripts/Snake.py')
        except:
            pass 

    @QtCore.pyqtSlot()
    def on_actionAngry_Birds_triggered(self):
        print('This is a test.')
        try:
            os.popen(f'cd scripts/FlyBrid/ && python flappy.py')
        except:
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

    window = QmyMianWindow()  # 第二步在应用上创建主窗口
    window.show()  # 显示主窗口所有内容

    sys.exit(app.exec_())  # 执行应用循环，固定步骤