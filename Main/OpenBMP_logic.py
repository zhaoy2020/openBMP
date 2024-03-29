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

import Blast.BlastGUI.LocalBlastGUI_logic as LocalBlastGUI_logic
import ToolBox.LigationCalculator.LigationCalculator_logic as LigationCalculator_logic
import ToolBox.MolarityCalculator.MolarityCalculator_logic as MolarityCalculator_logic
import ToolBox.RenameID.RenameID_logic as RenameID_logic
import Annotation.PGAP.PGAP_logic as PGAP_logic 
import ToolBox.Matplotlib.Matplotlib_logic as Matplotlib_logic
import ToolBox.MarkPDF.MarkPDF_logic as MarkPDF_logic

# import OpenBMP_ui  # 导入ui.py创建的类
from Main import OpenBMP_ui


# =============================================================================
# 编写逻辑部分
# =============================================================================
class QmyMianWindow(QtWidgets.QMainWindow):             # 使用单继承的方式进行操作
    '''
    主界面
    '''
    def __init__(self, parent=None):
        super().__init__(parent)                        # 初始化QtWidgets.QMainWindow这个父类的__init__方法,此时self就变成了QtWidgets.QMainWindow这个父类了
        self.ui = OpenBMP_ui.Ui_OpenBMP()               # 创建UI对象（实例化对象）
        self.ui.setupUi(self)                           # 构造UI，记得传self(QtWidgets.QMainWindow)

        self.ui.label_2.setOpenExternalLinks(True)      # 超链接至Github openBMP项目上

#  ===============================有connectSlotsByName()自动关联的槽函数===============================
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
    def on_actionMolarity_calculator_triggered(self):
        MolarityCalculator = MolarityCalculator_logic.QMolarityCalculator(self)
        MolarityCalculator.show()
        

    @QtCore.pyqtSlot()
    def on_actionLigation_Calculator_triggered(self):
        LigationCalculator = LigationCalculator_logic.QLigationCalculator(self)
        LigationCalculator.show()

    @QtCore.pyqtSlot()
    def on_actionRename_ID_triggered(self):
        RenameID = RenameID_logic.QRenameID(self)
        RenameID.show()

    @QtCore.pyqtSlot()
    def on_actionMatplotlib_triggered(self):
        matplotlibFigure = Matplotlib_logic.QMatplotlib(self)
        matplotlibFigure.show()

    @QtCore.pyqtSlot()
    def on_actionMarkPDF_triggered(self):
        markPDF = MarkPDF_logic.QMarkPDF(self)
        markPDF.show()

    @QtCore.pyqtSlot()
    def on_actionPGAP_triggered(self):
        '''open NCBI Prokaryotic Genome Annotation Pipeline window'''
        PGAP = PGAP_logic.QPGAP(self)
        PGAP.show()

    @QtCore.pyqtSlot()
    def on_actionQiime2_triggered(self):
        from Amplicon.Qiime import amplicon_logic
        qiime = amplicon_logic.QAmplicon(self)
        qiime.show()

    @QtCore.pyqtSlot()
    def on_actionGomoku_triggered(self):
        print('Start Gomoku.')
        try:
            # os.popen(f'python ./Scripts/Gomoku.py')               # 方法3
            # outBtypes = subprocess.check_output(['python', './Scripts/Gomoku.py'], stderr=subprocess.STDOUT)
            # print(outBtypes.decode('gbk'))                        # 方法2
            from Scripts import Gomoku
            Gomoku.runGame()                                        # 方法1
            # from concurrent.futures import ProcessPoolExecutor    # 方法4，开多进程池。结果仍然只能开一个程序
            # with ProcessPoolExecutor() as pool:
            #     pool.map(Gomoku.runGame())
        except:
            # QtWidgets.QMessageBox.warning(self, "错误", "执行错误！")
            pass

    @QtCore.pyqtSlot()
    def on_actionGreedy_Snake_triggered(self):
        print('Start Snake.')
        try:
            # os.popen(f'python ./Scripts/Snake.py')
            from Scripts import Snake
            Snake.runGame()
        except:
            # QtWidgets.QMessageBox.warning(self, "错误", "执行错误！")
            pass

    @QtCore.pyqtSlot()
    def on_actionAngry_Birds_triggered(self):
        print('Start FlyBrid')
        try:
            os.popen(f'cd scripts/FlyBrid/ && python flappy.py')
            # from Scripts.FlyBrid import flappy
            # flappy.runGame()
        except:
            # QtWidgets.QMessageBox.warning(self, "错误", "执行错误！")
            pass

#  ===============================自定义的槽函数===============================


if __name__ == "__main__":
    '''
    appMain创建应用程序和窗体，然后显示窗体，并开始运行应用程序；
    将ui.py文件的测试运行部分单独拿出来作为一个文件。
    当一个应用程序有多个窗体，并且窗体之间有数据传输时，
    appMain.py负责创建应用程序的主窗体并运行起来，
    这样整个应用程序的结构就更加清晰了。
    '''
    app = QtWidgets.QApplication(sys.argv)  # 第一步创建GUI应用程序，固定步骤

    window = QmyMianWindow()                # 第二步在应用上创建主窗口
    window.show()                           # 显示主窗口所有内容

    sys.exit(app.exec_())                   # 执行应用循环，固定步骤