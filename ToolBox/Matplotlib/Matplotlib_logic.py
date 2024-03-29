# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:01:17 2023

@author: zhao
"""
import numpy as np
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from PyQt5 import QtWidgets, QtCore
# import Matplotlib_ui
from ToolBox.Matplotlib import Matplotlib_ui

class QMatplotlib(QtWidgets.QMainWindow):
    '''
    Matplotlib逻辑部分
    '''
    def __init__(self, parent=None):
        super().__init__(parent)                                # 继承QtWidgets.QWidget
        self.ui = Matplotlib_ui.Ui_Matplotlib()
        self.ui.setupUi(self)
        mpl.rcParams['font.sans-serif']=['KaiTi','SimHei']                  #汉字字体
        mpl.rcParams['axes.unicode_minus'] =False                           #正常显示符号
        self.__iniFigure()                                                  # 创建绘图系统，初始化窗口
        self.__drawFigure()                                                 # 绘图
    #================自定义函数=====================
    def __iniFigure(self):
        self.__fig=mpl.figure.Figure(figsize=(8, 5))                        #单位英寸
        self.__fig.suptitle("plot in GUI application")                      #总的图标题
        figCanvas = FigureCanvas(self.__fig)                                #创建FigureCanvas对象，必须传递一个Figure对象

        naviToolbar=NavigationToolbar(figCanvas, self)                      #创建工具栏
        naviToolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)   #ToolButtonTextUnderIcon,ToolButtonTextBesideIcon

        self.addToolBar(naviToolbar)                                        #添加工具栏到主窗口
        self.setCentralWidget(figCanvas)

    def __drawFigure(self):                     ## 绘图
        t = np.linspace(0, 10, 40)
        y1=np.sin(t)
        y2=np.cos(2*t)
        ax1=self.__fig.add_subplot(1,2,1)       #添加子图，ax1是 matplotlib.axes.Axes 类对象
        ax1.plot(t,y1,'r-o',label="sin", linewidth=1, markersize=5)     #绘制一条曲线
        ax1.plot(t,y2,'b:',label="cos",linewidth=2)                     #绘制一条曲线
        ax1.set_xlabel('X 轴')                  # X轴标题
        ax1.set_ylabel('Y 轴',fontsize=14)      # Y轴标题
        ax1.set_xlim([0,10])                    # X轴范围 
        ax1.set_ylim([-1.5,1.5])                # Y轴范围 
        ax1.set_title("曲线")                   # 子图标题
        ax1.legend()                            # 自动创建图例

        ax2=self.__fig.add_subplot(1,2,2)   #添加子图，ax2是 matplotlib.axes.Axes 类对象
        week=["Mon","Tue","Wed","Thur","Fri","Sat","Sun"] 
        sales=np.random.randint(200,400,7)
        ax2.bar(week,sales)           # 绘制柱状图
        ax2.set_xlabel('week days')   # X轴标题
        ax2.set_ylabel('参观人数')    # Y轴标题
        ax2.set_title("柱状图")       # 子图标题
        # self.__fig.set_tight_layout(True) #紧凑布局

if __name__ == "__main__":
    '''
    appMain创建应用程序和窗体，然后显示窗体，并开始运行应用程序；
    将ui.py文件的测试运行部分单独拿出来作为一个文件。
    当一个应用程序有多个窗体，并且窗体之间有数据传输时，
    appMain.py负责创建应用程序的主窗体并运行起来，
    这样整个应用程序的结构就更加清晰了。
    '''
    app = QtWidgets.QApplication(sys.argv)  # 第一步创建GUI应用程序，固定步骤

    window = QMatplotlib()               # 第二步在应用上创建主窗口
    window.show()                           # 显示主窗口所有内容

    sys.exit(app.exec_())                   # 执行应用循环，固定步骤