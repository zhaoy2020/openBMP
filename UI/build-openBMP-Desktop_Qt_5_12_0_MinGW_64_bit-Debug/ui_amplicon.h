/********************************************************************************
** Form generated from reading UI file 'amplicon.ui'
**
** Created by: Qt User Interface Compiler version 5.12.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_AMPLICON_H
#define UI_AMPLICON_H

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

class Ui_amplicon
{
public:
    QWidget *centralwidget;
    QPushButton *pushButton;
    QLabel *label;
    QLineEdit *lineEdit;
    QLabel *label_2;
    QLineEdit *lineEdit_2;
    QPushButton *pushButton_2;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *amplicon)
    {
        if (amplicon->objectName().isEmpty())
            amplicon->setObjectName(QString::fromUtf8("amplicon"));
        amplicon->resize(800, 600);
        centralwidget = new QWidget(amplicon);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        pushButton = new QPushButton(centralwidget);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(260, 70, 80, 15));
        label = new QLabel(centralwidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(70, 60, 61, 31));
        lineEdit = new QLineEdit(centralwidget);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));
        lineEdit->setGeometry(QRect(140, 70, 113, 20));
        label_2 = new QLabel(centralwidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(70, 110, 61, 31));
        lineEdit_2 = new QLineEdit(centralwidget);
        lineEdit_2->setObjectName(QString::fromUtf8("lineEdit_2"));
        lineEdit_2->setGeometry(QRect(140, 110, 113, 20));
        pushButton_2 = new QPushButton(centralwidget);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));
        pushButton_2->setGeometry(QRect(270, 110, 80, 15));
        amplicon->setCentralWidget(centralwidget);
        menubar = new QMenuBar(amplicon);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 800, 17));
        amplicon->setMenuBar(menubar);
        statusbar = new QStatusBar(amplicon);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        amplicon->setStatusBar(statusbar);

        retranslateUi(amplicon);

        QMetaObject::connectSlotsByName(amplicon);
    } // setupUi

    void retranslateUi(QMainWindow *amplicon)
    {
        amplicon->setWindowTitle(QApplication::translate("amplicon", "MainWindow", nullptr));
        pushButton->setText(QApplication::translate("amplicon", "Open metadata", nullptr));
        label->setText(QApplication::translate("amplicon", "Metadata path", nullptr));
        label_2->setText(QApplication::translate("amplicon", "Raw data", nullptr));
        pushButton_2->setText(QApplication::translate("amplicon", "Open fastq dir.", nullptr));
    } // retranslateUi

};

namespace Ui {
    class amplicon: public Ui_amplicon {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_AMPLICON_H
