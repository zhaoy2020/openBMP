/********************************************************************************
** Form generated from reading UI file 'Matplotlib.ui'
**
** Created by: Qt User Interface Compiler version 5.12.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MATPLOTLIB_H
#define UI_MATPLOTLIB_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Matplotlib
{
public:
    QWidget *centralwidget;
    QPushButton *pushButton;
    QLabel *label;
    QLineEdit *lineEdit;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *Matplotlib)
    {
        if (Matplotlib->objectName().isEmpty())
            Matplotlib->setObjectName(QString::fromUtf8("Matplotlib"));
        Matplotlib->resize(800, 600);
        centralwidget = new QWidget(Matplotlib);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        pushButton = new QPushButton(centralwidget);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(320, 120, 80, 15));
        label = new QLabel(centralwidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(140, 130, 41, 9));
        lineEdit = new QLineEdit(centralwidget);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));
        lineEdit->setGeometry(QRect(190, 120, 113, 20));
        Matplotlib->setCentralWidget(centralwidget);
        menubar = new QMenuBar(Matplotlib);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 800, 17));
        Matplotlib->setMenuBar(menubar);
        statusbar = new QStatusBar(Matplotlib);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        Matplotlib->setStatusBar(statusbar);

        retranslateUi(Matplotlib);

        QMetaObject::connectSlotsByName(Matplotlib);
    } // setupUi

    void retranslateUi(QMainWindow *Matplotlib)
    {
        Matplotlib->setWindowTitle(QApplication::translate("Matplotlib", "MainWindow", nullptr));
        pushButton->setText(QApplication::translate("Matplotlib", "PushButton", nullptr));
        label->setText(QApplication::translate("Matplotlib", "TextLabel", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Matplotlib: public Ui_Matplotlib {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MATPLOTLIB_H
