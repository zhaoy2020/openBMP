# -*- coding: utf-8 -*-
"""
Created on Mon May 22 14:29:31 2023

@author: zhao
"""

from Bio import SeqIO
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
        try:
            curPath = os.getcwd()
            self.QueryFileName, flt = QtWidgets.QFileDialog.getOpenFileName(self, "选择Query路径", curPath, "文本文件(*.fasta;*.ffn;*.fnn;*.ffa;*.faa;*.fa);;所有文件(*.*)")
            print(f"导入文件{self.QueryFileName}")
            print(f"文件类型为{flt}")
            self.ui.lineEdit.setText(self.QueryFileName)
        except:
            QtWidgets.QMessageBox.warning(self, "错误", "不能为空！")

    @QtCore.pyqtSlot()
    def on_pushButton_2_clicked(self):
        try:
            self.outputFile, outputFileFormat = QtWidgets.QFileDialog.getSaveFileName(self, '选择保存的路径')
            print(f'保存至：{self.outputFile}')
            print(f'文件类型为：{outputFileFormat}')
            self.ui.lineEdit_2.setText(self.outputFile)
        except:
            QtWidgets.QMessageBox.warning(self, "错误", "不能为空！")
            

    def extract_seq(self, db_handle, extract_list):
        '''从fasta数据库中，按要求提取序列
            db_handle:数据库的位置
            extract_list:要提取的序列列表,dataframe格式
            函数最终返回的的含有SeqRecord类的列表
        '''
        # db可以存在重复序列，全部提取出来，但是遇到大序列时候比较慢
        store = []  # 临时存放Bio.SeqRecord对象
        num = 0  # 计数
        success_list = []
        num_no = 0
        END = len( [i for i in SeqIO.parse(db_handle, format='fasta')] )

        for rec_extr in extract_list:
            counter = 0
            for rec in SeqIO.parse(db_handle, format='fasta'):
                counter += 1
                if rec_extr == rec.id:      # 一定要用id，而不是name，虽然内容是一样的，但到SeqIO.write（）时候只能识别id
                    print(counter, rec.id)
                    num += 1           # 序号和计数
                    print('正在提取', rec.id, rec.description, num)
                    self.ui.textBrowser.append(f"正在提取\t{rec.id}\t{num}")
                    if rec.seq:             # 判断rec是否为空，不为空则添加到store列表中，表示成功提取
                        store.append(rec)
                        success_list.append(rec_extr)
                        print('成功', len(rec.seq),'bp')
                        self.ui.textBrowser.append(f"成功\t{len(rec.seq)} bp")
                    else:
                        print('序列为空！')
                        self.ui.textBrowser.append(f"序列为空")
                else:
                    if counter == END:
                         if rec_extr not in success_list:
                            print(rec.id)
                            num_no += 1
                            print(f'{rec_extr}提取失败\t{num_no}')
                            self.ui.textBrowser.append(f'{rec_extr}\t提取失败\t{num_no}')
        if store:
            print('提取完成\n')
            self.ui.textBrowser.append(f"提取完成: {num} 成功, {num_no} 失败\t{'='*10}")
        else:
            print('无对应序列，提取失败！！！')
            self.ui.textBrowser.append(f"{extract_list}\t无对应序列，提取失败！！！{'='*10}")
        return store
        '''
        # 忽略db中重复序列，但是遇到大序列时候比较快
        store = []  # 临时存放Bio.SeqRecord对象
        num = 0  # 计数
        num_no = 0
        db = SeqIO.parse(db_handle, format='fasta')
        db_id_dic = {rec.id:rec for rec in db}
        for rec_extr in extract_list:   ### 会忽略db中的重复名称的序列
            if rec_extr in db_id_dic.keys():
                num += 1  # 序号和计数
                print('正在提取', rec_extr, num)
                self.ui.textBrowser.append(f"正在提取\t{rec_extr}\t{num}")
                if db_id_dic.get(rec_extr).seq:  # 判断rec是否为空，不为空则添加到store列表中，表示成功提取
                    store.append(db_id_dic.get(rec_extr))
                    print('成功',len(db_id_dic.get(rec_extr).seq),'bp')
                    self.ui.textBrowser.append(f"成功\t{len(db_id_dic.get(rec_extr).seq)} bp")
                else:
                    print('序列为空！')
                    self.ui.textBrowser.append(f"序列为空")
            else:
                num_no += 1
                print(f'{rec_extr}提取失败\t{num_no}')
                self.ui.textBrowser.append(f'{rec_extr}\t提取失败\t{num_no}')
        if store:
            print('提取完成\n')
            self.ui.textBrowser.append(f"提取完成: {num} 成功, {num_no} 失败\t{'='*10}")
        else:
            print('无对应序列，提取失败！！！')
            self.ui.textBrowser.append(f"{extract_list}\t无对应序列，提取失败！！！{'='*10}")
        return store
    '''
    
    @QtCore.pyqtSlot()
    def on_pushButton_5_clicked(self):
        '''extract'''
        try:
            ids = self.ui.textEdit.toPlainText()
            ids_list = ids.split()
            print(f'提取：{ids_list}')
            SeqIO.write(self.extract_seq(self.QueryFileName, ids_list), self.outputFile, "fasta")
        except:
            QtWidgets.QMessageBox.warning(self, "错误", "提取错误！")

    @QtCore.pyqtSlot()
    def on_pushButton_6_clicked(self):
        '''clear'''
        try:
            self.ui.textEdit.setPlainText('')
        except:
            QtWidgets.QMessageBox.warning(self, "错误", "无法清除！")


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