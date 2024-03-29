/********************************************************************************
** Form generated from reading UI file 'RenameID.ui'
**
** Created by: Qt User Interface Compiler version 5.12.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_RENAMEID_H
#define UI_RENAMEID_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_RenameID
{
public:
    QVBoxLayout *verticalLayout;
    QLabel *label_3;
    QGroupBox *groupBox_2;
    QGridLayout *gridLayout;
    QLabel *label;
    QLabel *label_2;
    QPushButton *pushButton;
    QLineEdit *lineEdit;
    QLineEdit *lineEdit_2;
    QPushButton *pushButton_2;
    QGroupBox *groupBox;
    QVBoxLayout *verticalLayout_2;
    QTextEdit *textEdit;
    QPushButton *pushButton_3;
    QHBoxLayout *horizontalLayout;
    QSpacerItem *horizontalSpacer;
    QPushButton *pushButton_4;
    QSpacerItem *horizontalSpacer_3;
    QPushButton *pushButton_5;
    QSpacerItem *horizontalSpacer_2;

    void setupUi(QDialog *RenameID)
    {
        if (RenameID->objectName().isEmpty())
            RenameID->setObjectName(QString::fromUtf8("RenameID"));
        RenameID->resize(326, 307);
        QFont font;
        font.setFamily(QString::fromUtf8("Times New Roman"));
        RenameID->setFont(font);
        verticalLayout = new QVBoxLayout(RenameID);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        label_3 = new QLabel(RenameID);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setAlignment(Qt::AlignCenter);

        verticalLayout->addWidget(label_3);

        groupBox_2 = new QGroupBox(RenameID);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        gridLayout = new QGridLayout(groupBox_2);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label = new QLabel(groupBox_2);
        label->setObjectName(QString::fromUtf8("label"));
        label->setAlignment(Qt::AlignCenter);

        gridLayout->addWidget(label, 0, 0, 1, 1);

        label_2 = new QLabel(groupBox_2);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setAlignment(Qt::AlignCenter);

        gridLayout->addWidget(label_2, 1, 0, 1, 1);

        pushButton = new QPushButton(groupBox_2);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        gridLayout->addWidget(pushButton, 0, 2, 1, 1);

        lineEdit = new QLineEdit(groupBox_2);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));

        gridLayout->addWidget(lineEdit, 0, 1, 1, 1);

        lineEdit_2 = new QLineEdit(groupBox_2);
        lineEdit_2->setObjectName(QString::fromUtf8("lineEdit_2"));

        gridLayout->addWidget(lineEdit_2, 1, 1, 1, 1);

        pushButton_2 = new QPushButton(groupBox_2);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));

        gridLayout->addWidget(pushButton_2, 1, 2, 1, 1);


        verticalLayout->addWidget(groupBox_2);

        groupBox = new QGroupBox(RenameID);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        verticalLayout_2 = new QVBoxLayout(groupBox);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        textEdit = new QTextEdit(groupBox);
        textEdit->setObjectName(QString::fromUtf8("textEdit"));

        verticalLayout_2->addWidget(textEdit);

        pushButton_3 = new QPushButton(groupBox);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));
        QSizePolicy sizePolicy(QSizePolicy::Minimum, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(pushButton_3->sizePolicy().hasHeightForWidth());
        pushButton_3->setSizePolicy(sizePolicy);

        verticalLayout_2->addWidget(pushButton_3);


        verticalLayout->addWidget(groupBox);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        pushButton_4 = new QPushButton(RenameID);
        pushButton_4->setObjectName(QString::fromUtf8("pushButton_4"));

        horizontalLayout->addWidget(pushButton_4);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_3);

        pushButton_5 = new QPushButton(RenameID);
        pushButton_5->setObjectName(QString::fromUtf8("pushButton_5"));

        horizontalLayout->addWidget(pushButton_5);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_2);


        verticalLayout->addLayout(horizontalLayout);


        retranslateUi(RenameID);

        QMetaObject::connectSlotsByName(RenameID);
    } // setupUi

    void retranslateUi(QDialog *RenameID)
    {
        RenameID->setWindowTitle(QApplication::translate("RenameID", "Rename ID", nullptr));
        label_3->setText(QApplication::translate("RenameID", "<html><head/><body><p><span style=\" font-size:12pt;\">Rename ID and extract of FASTA-related files</span></p></body></html>", nullptr));
        groupBox_2->setTitle(QApplication::translate("RenameID", "Files", nullptr));
        label->setText(QApplication::translate("RenameID", "Input FASTA", nullptr));
        label_2->setText(QApplication::translate("RenameID", "Output FASTA", nullptr));
        pushButton->setText(QApplication::translate("RenameID", "File", nullptr));
        pushButton_2->setText(QApplication::translate("RenameID", "File", nullptr));
        groupBox->setTitle(QApplication::translate("RenameID", "Match table", nullptr));
        pushButton_3->setText(QApplication::translate("RenameID", "File", nullptr));
        pushButton_4->setText(QApplication::translate("RenameID", "Rename", nullptr));
        pushButton_5->setText(QApplication::translate("RenameID", "Extract", nullptr));
    } // retranslateUi

};

namespace Ui {
    class RenameID: public Ui_RenameID {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_RENAMEID_H
