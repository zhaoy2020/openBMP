/********************************************************************************
** Form generated from reading UI file 'LocalBlastGUI.ui'
**
** Created by: Qt User Interface Compiler version 5.12.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_LOCALBLASTGUI_H
#define UI_LOCALBLASTGUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDoubleSpinBox>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_LocalBlastGUI
{
public:
    QVBoxLayout *verticalLayout_2;
    QGroupBox *groupBox;
    QGridLayout *gridLayout;
    QLabel *label;
    QLineEdit *lineEdit;
    QPushButton *pushButton;
    QLabel *label_2;
    QLineEdit *lineEdit_2;
    QPushButton *pushButton_2;
    QLabel *label_3;
    QLineEdit *lineEdit_3;
    QPushButton *pushButton_3;
    QGroupBox *groupBox_2;
    QGridLayout *gridLayout_2;
    QPushButton *pushButton_4;
    QPushButton *pushButton_5;
    QPushButton *pushButton_6;
    QGroupBox *groupBox_3;
    QFormLayout *formLayout;
    QLabel *label_4;
    QComboBox *comboBox;
    QLabel *label_5;
    QSpinBox *spinBox;
    QLabel *label_6;
    QSpinBox *spinBox_2;
    QLabel *label_7;
    QSpinBox *spinBox_3;
    QLabel *label_8;
    QLabel *label_9;
    QSpinBox *spinBox_5;
    QLabel *label_10;
    QComboBox *comboBox_2;
    QDoubleSpinBox *doubleSpinBox_4;
    QGroupBox *groupBox_4;
    QVBoxLayout *verticalLayout;
    QTextBrowser *textBrowser;

    void setupUi(QWidget *LocalBlastGUI)
    {
        if (LocalBlastGUI->objectName().isEmpty())
            LocalBlastGUI->setObjectName(QString::fromUtf8("LocalBlastGUI"));
        LocalBlastGUI->resize(285, 461);
        verticalLayout_2 = new QVBoxLayout(LocalBlastGUI);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        groupBox = new QGroupBox(LocalBlastGUI);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        gridLayout = new QGridLayout(groupBox);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label = new QLabel(groupBox);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout->addWidget(label, 0, 0, 1, 1);

        lineEdit = new QLineEdit(groupBox);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));

        gridLayout->addWidget(lineEdit, 0, 1, 1, 1);

        pushButton = new QPushButton(groupBox);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        gridLayout->addWidget(pushButton, 0, 2, 1, 1);

        label_2 = new QLabel(groupBox);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout->addWidget(label_2, 1, 0, 1, 1);

        lineEdit_2 = new QLineEdit(groupBox);
        lineEdit_2->setObjectName(QString::fromUtf8("lineEdit_2"));

        gridLayout->addWidget(lineEdit_2, 1, 1, 1, 1);

        pushButton_2 = new QPushButton(groupBox);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));

        gridLayout->addWidget(pushButton_2, 1, 2, 1, 1);

        label_3 = new QLabel(groupBox);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout->addWidget(label_3, 2, 0, 1, 1);

        lineEdit_3 = new QLineEdit(groupBox);
        lineEdit_3->setObjectName(QString::fromUtf8("lineEdit_3"));

        gridLayout->addWidget(lineEdit_3, 2, 1, 1, 1);

        pushButton_3 = new QPushButton(groupBox);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));

        gridLayout->addWidget(pushButton_3, 2, 2, 1, 1);


        verticalLayout_2->addWidget(groupBox);

        groupBox_2 = new QGroupBox(LocalBlastGUI);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        gridLayout_2 = new QGridLayout(groupBox_2);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        pushButton_4 = new QPushButton(groupBox_2);
        pushButton_4->setObjectName(QString::fromUtf8("pushButton_4"));

        gridLayout_2->addWidget(pushButton_4, 0, 0, 1, 1);

        pushButton_5 = new QPushButton(groupBox_2);
        pushButton_5->setObjectName(QString::fromUtf8("pushButton_5"));

        gridLayout_2->addWidget(pushButton_5, 0, 1, 1, 1);

        pushButton_6 = new QPushButton(groupBox_2);
        pushButton_6->setObjectName(QString::fromUtf8("pushButton_6"));

        gridLayout_2->addWidget(pushButton_6, 0, 2, 1, 1);


        verticalLayout_2->addWidget(groupBox_2);

        groupBox_3 = new QGroupBox(LocalBlastGUI);
        groupBox_3->setObjectName(QString::fromUtf8("groupBox_3"));
        formLayout = new QFormLayout(groupBox_3);
        formLayout->setObjectName(QString::fromUtf8("formLayout"));
        label_4 = new QLabel(groupBox_3);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setAlignment(Qt::AlignCenter);

        formLayout->setWidget(0, QFormLayout::LabelRole, label_4);

        comboBox = new QComboBox(groupBox_3);
        comboBox->setObjectName(QString::fromUtf8("comboBox"));

        formLayout->setWidget(0, QFormLayout::FieldRole, comboBox);

        label_5 = new QLabel(groupBox_3);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setAlignment(Qt::AlignCenter);

        formLayout->setWidget(1, QFormLayout::LabelRole, label_5);

        spinBox = new QSpinBox(groupBox_3);
        spinBox->setObjectName(QString::fromUtf8("spinBox"));

        formLayout->setWidget(1, QFormLayout::FieldRole, spinBox);

        label_6 = new QLabel(groupBox_3);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        formLayout->setWidget(2, QFormLayout::LabelRole, label_6);

        spinBox_2 = new QSpinBox(groupBox_3);
        spinBox_2->setObjectName(QString::fromUtf8("spinBox_2"));

        formLayout->setWidget(2, QFormLayout::FieldRole, spinBox_2);

        label_7 = new QLabel(groupBox_3);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        formLayout->setWidget(3, QFormLayout::LabelRole, label_7);

        spinBox_3 = new QSpinBox(groupBox_3);
        spinBox_3->setObjectName(QString::fromUtf8("spinBox_3"));

        formLayout->setWidget(3, QFormLayout::FieldRole, spinBox_3);

        label_8 = new QLabel(groupBox_3);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        formLayout->setWidget(4, QFormLayout::LabelRole, label_8);

        label_9 = new QLabel(groupBox_3);
        label_9->setObjectName(QString::fromUtf8("label_9"));

        formLayout->setWidget(5, QFormLayout::LabelRole, label_9);

        spinBox_5 = new QSpinBox(groupBox_3);
        spinBox_5->setObjectName(QString::fromUtf8("spinBox_5"));

        formLayout->setWidget(5, QFormLayout::FieldRole, spinBox_5);

        label_10 = new QLabel(groupBox_3);
        label_10->setObjectName(QString::fromUtf8("label_10"));
        label_10->setAlignment(Qt::AlignCenter);

        formLayout->setWidget(6, QFormLayout::LabelRole, label_10);

        comboBox_2 = new QComboBox(groupBox_3);
        comboBox_2->setObjectName(QString::fromUtf8("comboBox_2"));

        formLayout->setWidget(6, QFormLayout::FieldRole, comboBox_2);

        doubleSpinBox_4 = new QDoubleSpinBox(groupBox_3);
        doubleSpinBox_4->setObjectName(QString::fromUtf8("doubleSpinBox_4"));

        formLayout->setWidget(4, QFormLayout::FieldRole, doubleSpinBox_4);


        verticalLayout_2->addWidget(groupBox_3);

        groupBox_4 = new QGroupBox(LocalBlastGUI);
        groupBox_4->setObjectName(QString::fromUtf8("groupBox_4"));
        verticalLayout = new QVBoxLayout(groupBox_4);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        textBrowser = new QTextBrowser(groupBox_4);
        textBrowser->setObjectName(QString::fromUtf8("textBrowser"));

        verticalLayout->addWidget(textBrowser);


        verticalLayout_2->addWidget(groupBox_4);


        retranslateUi(LocalBlastGUI);

        QMetaObject::connectSlotsByName(LocalBlastGUI);
    } // setupUi

    void retranslateUi(QWidget *LocalBlastGUI)
    {
        LocalBlastGUI->setWindowTitle(QApplication::translate("LocalBlastGUI", "Local Blast GUI", nullptr));
        groupBox->setTitle(QApplication::translate("LocalBlastGUI", "Work station", nullptr));
        label->setText(QApplication::translate("LocalBlastGUI", "DB path", nullptr));
        pushButton->setText(QApplication::translate("LocalBlastGUI", "File", nullptr));
        label_2->setText(QApplication::translate("LocalBlastGUI", "Query path", nullptr));
        pushButton_2->setText(QApplication::translate("LocalBlastGUI", "File", nullptr));
        label_3->setText(QApplication::translate("LocalBlastGUI", "Output path", nullptr));
        pushButton_3->setText(QApplication::translate("LocalBlastGUI", "Dir.", nullptr));
        groupBox_2->setTitle(QApplication::translate("LocalBlastGUI", "Command", nullptr));
        pushButton_4->setText(QApplication::translate("LocalBlastGUI", "Format DB", nullptr));
        pushButton_5->setText(QApplication::translate("LocalBlastGUI", "Blast", nullptr));
        pushButton_6->setText(QApplication::translate("LocalBlastGUI", "Default parameters", nullptr));
        groupBox_3->setTitle(QApplication::translate("LocalBlastGUI", "Parameters", nullptr));
        label_4->setText(QApplication::translate("LocalBlastGUI", "dbtype", nullptr));
        label_5->setText(QApplication::translate("LocalBlastGUI", "CPU threads", nullptr));
        label_6->setText(QApplication::translate("LocalBlastGUI", "max_hsps", nullptr));
        label_7->setText(QApplication::translate("LocalBlastGUI", "num_aligments", nullptr));
        label_8->setText(QApplication::translate("LocalBlastGUI", "Evalue", nullptr));
        label_9->setText(QApplication::translate("LocalBlastGUI", "outfmt", nullptr));
        label_10->setText(QApplication::translate("LocalBlastGUI", "Blasttype", nullptr));
        groupBox_4->setTitle(QApplication::translate("LocalBlastGUI", "Termininal", nullptr));
    } // retranslateUi

};

namespace Ui {
    class LocalBlastGUI: public Ui_LocalBlastGUI {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LOCALBLASTGUI_H
