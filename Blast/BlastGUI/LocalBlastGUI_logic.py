# -*- coding: utf-8 -*-
"""
Created on Thu May 11 11:26:25 2023
LocalBalstGUI逻辑部分
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

# =============================================================================
# class Signal(QtCore.QObject):
#     text_update = QtCore.pyqtSignal(str)
# 
#     def write(self, text):
#         self.text_update.emit(str(text))
#         # loop = QEventLoop()
#         # QTimer.singleShot(100, loop.quit)
#         # loop.exec_()
#         QtWidgets.QApplication.processEvents()
# =============================================================================

# =============================================================================
# 编译LocalBlastGUI.ui至py文件
# =============================================================================
# uiName = "LocalBlastGUI"
# # 放在UI文件夹下面
# uicmd = f'D:\ProgramFiles\miniconda3\python -m PyQt5.uic.pyuic UI/openBMP/{uiName}.ui -o {uiName}_ui.py'
# os.system(uicmd)  # 先将UI文件转格式为py格式文件
# import LocalBlastGUI_ui  # 导入ui.py创建的类
from Blast.BlastGUI import LocalBlastGUI_ui


class QLocalBlastGUI(QtWidgets.QWidget):
    '''
    LocalBlastGUI逻辑部分
    '''
    def __init__(self, parent=None):
        super().__init__(parent) # 继承QtWidgets.QWidget
        self.ui = LocalBlastGUI_ui.Ui_LocalBlastGUI()
        self.ui.setupUi(self)
        
# =============================================================================
#         # 实时显示输出, 将控制台的输出重定向到界面中
#         sys.stdout = Signal()
#         sys.stdout.text_update.connect(self.updatetext)
#     def updatetext(self, text):
#         """
#             更新textBrowser
#         """
#         cursor = self.ui.textBrowser.textCursor()
#         cursor.movePosition(QtGui.QTextCursor.End)
#         self.ui.textBrowser.append(text)
#         self.ui.textBrowser.setTextCursor(cursor)
#         self.ui.textBrowser.ensureCursorVisible()
# =============================================================================

##  ===============================有connectSlotsByName()自动关联的槽函数===============================
    @QtCore.pyqtSlot()
    def on_pushButton_6_clicked(self):
        self.ui.spinBox.setValue(2)                     # cpu threads -> 2
        self.ui.spinBox_2.setValue(1)                   # max_hsps -> 1
        self.ui.spinBox_3.setValue(1)                   # num_aligments -> 1
        self.ui.doubleSpinBox_4.setValue(0.00001)       # Evlaue -> 0.00001
        self.ui.spinBox_5.setValue(6)                   # outfmt -> 6

    @QtCore.pyqtSlot()
    def on_pushButton_clicked(self):
        '''DB fasta'''
        try:
            curPath = os.getcwd()
            self.DBFileName, DBflt = QtWidgets.QFileDialog.getOpenFileName(self, "选择DB路径", curPath, "文本文件(*.fasta;*.ffn;*.fnn;*.ffa;*.faa;*.fa);;所有文件(*.*)")
            print(f"导入文件{self.DBFileName}")
            print(f"文件类型为{DBflt}")
            self.ui.textBrowser.append(f"导入文件{self.DBFileName}")
            self.ui.textBrowser.append(f"文件类型为{DBflt}")
            # self.ui.textBrowser.moveCursor(self.textBrowser.textCursor().End)
            self.ui.lineEdit.setText(self.DBFileName)
        except:
            pass

    @QtCore.pyqtSlot()
    def on_pushButton_2_clicked(self):
        '''Query fasta'''
        try:
            curPath = os.getcwd()
            self.QueryFileName, flt = QtWidgets.QFileDialog.getOpenFileName(self, "选择Query路径", curPath, "文本文件(*.fasta;*.ffn;*.fnn;*.ffa;*.faa,*.fa);;所有文件(*.*)")
            print(f"导入文件{self.QueryFileName}")
            print(f"文件类型为{flt}")
            self.ui.textBrowser.append(f"导入文件{self.QueryFileName}")
            self.ui.textBrowser.append(f"文件类型为{flt}")
            # self.ui.textBrowser.moveCursor(self.textBrowser.textCursor().End)
            self.ui.lineEdit_2.setText(self.QueryFileName)
        except:
            pass 

    @QtCore.pyqtSlot()
    def on_pushButton_3_clicked(self):
        '''output dir.'''
        try:
            self.outputDir = QtWidgets.QFileDialog.getExistingDirectory(self, "选择输出路径")
            print(f"输出文件位置{self.outputDir}")
            self.ui.textBrowser.append(f"输出文件位置{self.outputDir}")
            # self.ui.textBrowser.moveCursor(self.textBrowser.textCursor().End)
            self.ui.lineEdit_3.setText(self.outputDir)
        except:
            pass 

    @QtCore.pyqtSlot()
    def on_pushButton_4_clicked(self):
        '''DBformat'''
        try:
            makeDBcmd = f"\
                makeblastdb.exe \
                -dbtype {self.ui.comboBox.currentText()} \
                    -in {self.DBFileName} \
                        -parse_seqids \
                                -out {self.DBFileName.split('.')[0]}"
            print("start:\n",makeDBcmd)
            os.system(makeDBcmd)
            self.ui.textBrowser.append(f"start: {makeDBcmd}")
            # self.ui.textBrowser.moveCursor(self.textBrowser.textCursor().End)
        except :
            QtWidgets.QMessageBox.warning(self, "warining", "system errors")


    @QtCore.pyqtSlot()
    def on_pushButton_5_clicked(self):
        '''blast'''
        try:
            if self.ui.spinBox_5.value() == 6:
                blastcmd = f'''{self.ui.comboBox_2.currentText().split(" ")[0]} -num_threads {self.ui.spinBox.value()} -query {self.QueryFileName} -db {self.DBFileName.split('.')[0]} -out {self.outputDir}/{os.path.basename(self.QueryFileName).split('.')[0]}_results.txt -max_hsps {self.ui.spinBox_2.value()} -num_alignments {self.ui.spinBox_3.value()} -evalue {self.ui.doubleSpinBox_4.value()} -outfmt "{self.ui.spinBox_5.value()} qseqid sseqid sgi stitle evalue bitscore pident qcovs length mismatch gapopen qstart qend sstart send"'''
            else:
                blastcmd = f'''{self.ui.comboBox_2.currentText().split(" ")[0]} -num_threads {self.ui.spinBox.value()} -query {self.QueryFileName} -db {self.DBFileName.split('.')[0]} -out {self.outputDir}/{os.path.basename(self.QueryFileName).split('.')[0]}_results.txt -max_hsps {self.ui.spinBox_2.value()} -num_alignments {self.ui.spinBox_3.value()} -evalue {self.ui.doubleSpinBox_4.value()} -outfmt {self.ui.spinBox_5.value()}'''
            print(blastcmd)
            os.system(blastcmd)
            self.ui.textBrowser.append(f"start: {blastcmd}")
            # self.ui.textBrowser.moveCursor(self.textBrowser.textCursor().End)
        except:
            QtWidgets.QMessageBox.warning(self, "warining", "system errors")


if __name__ == "__main__":
    '''
    appMain创建应用程序和窗体，然后显示窗体，并开始运行应用程序；
    将ui.py文件的测试运行部分单独拿出来作为一个文件。
    当一个应用程序有多个窗体，并且窗体之间有数据传输时，
    appMain.py负责创建应用程序的主窗体并运行起来，
    这样整个应用程序的结构就更加清晰了。
    '''
    app = QtWidgets.QApplication(sys.argv)  # 第一步创建GUI应用程序，固定步骤

    window = QLocalBlastGUI()               # 第二步在应用上创建主窗口
    window.show()                           # 显示主窗口所有内容

    sys.exit(app.exec_())                   # 执行应用循环，固定步骤