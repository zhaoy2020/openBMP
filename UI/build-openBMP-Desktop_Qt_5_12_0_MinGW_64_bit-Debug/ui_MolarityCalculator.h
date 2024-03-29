/********************************************************************************
** Form generated from reading UI file 'MolarityCalculator.ui'
**
** Created by: Qt User Interface Compiler version 5.12.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MOLARITYCALCULATOR_H
#define UI_MOLARITYCALCULATOR_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MolarityCalculator
{
public:
    QVBoxLayout *verticalLayout_2;
    QGroupBox *groupBox_2;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *label_5;
    QLineEdit *lineEdit;
    QComboBox *comboBox_2;
    QLabel *label_2;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label_6;
    QLineEdit *lineEdit_2;
    QComboBox *comboBox;
    QLabel *label_3;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label_7;
    QLineEdit *lineEdit_3;
    QComboBox *comboBox_3;
    QLabel *label_4;
    QHBoxLayout *horizontalLayout_4;
    QLabel *label;
    QLineEdit *lineEdit_5;
    QPushButton *pushButton_3;
    QLabel *label_8;
    QLineEdit *lineEdit_4;
    QComboBox *comboBox_4;
    QHBoxLayout *horizontalLayout_5;
    QSpacerItem *horizontalSpacer;
    QPushButton *pushButton;
    QSpacerItem *horizontalSpacer_2;
    QPushButton *pushButton_2;
    QSpacerItem *horizontalSpacer_3;

    void setupUi(QWidget *MolarityCalculator)
    {
        if (MolarityCalculator->objectName().isEmpty())
            MolarityCalculator->setObjectName(QString::fromUtf8("MolarityCalculator"));
        MolarityCalculator->resize(308, 216);
        QFont font;
        font.setFamily(QString::fromUtf8("Times New Roman"));
        MolarityCalculator->setFont(font);
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/icons/images/DNA.svg"), QSize(), QIcon::Normal, QIcon::On);
        MolarityCalculator->setWindowIcon(icon);
        verticalLayout_2 = new QVBoxLayout(MolarityCalculator);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        groupBox_2 = new QGroupBox(MolarityCalculator);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        verticalLayout = new QVBoxLayout(groupBox_2);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label_5 = new QLabel(groupBox_2);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        horizontalLayout->addWidget(label_5);

        lineEdit = new QLineEdit(groupBox_2);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));

        horizontalLayout->addWidget(lineEdit);

        comboBox_2 = new QComboBox(groupBox_2);
        comboBox_2->addItem(QString());
        comboBox_2->addItem(QString());
        comboBox_2->addItem(QString());
        comboBox_2->addItem(QString());
        comboBox_2->addItem(QString());
        comboBox_2->setObjectName(QString::fromUtf8("comboBox_2"));

        horizontalLayout->addWidget(comboBox_2);


        verticalLayout->addLayout(horizontalLayout);

        label_2 = new QLabel(groupBox_2);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setAlignment(Qt::AlignCenter);

        verticalLayout->addWidget(label_2);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label_6 = new QLabel(groupBox_2);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        horizontalLayout_2->addWidget(label_6);

        lineEdit_2 = new QLineEdit(groupBox_2);
        lineEdit_2->setObjectName(QString::fromUtf8("lineEdit_2"));

        horizontalLayout_2->addWidget(lineEdit_2);

        comboBox = new QComboBox(groupBox_2);
        comboBox->addItem(QString());
        comboBox->addItem(QString());
        comboBox->addItem(QString());
        comboBox->addItem(QString());
        comboBox->setObjectName(QString::fromUtf8("comboBox"));

        horizontalLayout_2->addWidget(comboBox);


        verticalLayout->addLayout(horizontalLayout_2);

        label_3 = new QLabel(groupBox_2);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setAlignment(Qt::AlignCenter);

        verticalLayout->addWidget(label_3);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        label_7 = new QLabel(groupBox_2);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        horizontalLayout_3->addWidget(label_7);

        lineEdit_3 = new QLineEdit(groupBox_2);
        lineEdit_3->setObjectName(QString::fromUtf8("lineEdit_3"));

        horizontalLayout_3->addWidget(lineEdit_3);

        comboBox_3 = new QComboBox(groupBox_2);
        comboBox_3->addItem(QString());
        comboBox_3->addItem(QString());
        comboBox_3->addItem(QString());
        comboBox_3->addItem(QString());
        comboBox_3->setObjectName(QString::fromUtf8("comboBox_3"));

        horizontalLayout_3->addWidget(comboBox_3);


        verticalLayout->addLayout(horizontalLayout_3);

        label_4 = new QLabel(groupBox_2);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setAlignment(Qt::AlignCenter);

        verticalLayout->addWidget(label_4);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        label = new QLabel(groupBox_2);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout_4->addWidget(label);

        lineEdit_5 = new QLineEdit(groupBox_2);
        lineEdit_5->setObjectName(QString::fromUtf8("lineEdit_5"));

        horizontalLayout_4->addWidget(lineEdit_5);

        pushButton_3 = new QPushButton(groupBox_2);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));
        pushButton_3->setEnabled(true);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(pushButton_3->sizePolicy().hasHeightForWidth());
        pushButton_3->setSizePolicy(sizePolicy);
        QFont font1;
        font1.setPointSize(9);
        pushButton_3->setFont(font1);
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/icons/images/save.svg"), QSize(), QIcon::Normal, QIcon::On);
        pushButton_3->setIcon(icon1);
        pushButton_3->setIconSize(QSize(12, 12));

        horizontalLayout_4->addWidget(pushButton_3);

        label_8 = new QLabel(groupBox_2);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        horizontalLayout_4->addWidget(label_8);

        lineEdit_4 = new QLineEdit(groupBox_2);
        lineEdit_4->setObjectName(QString::fromUtf8("lineEdit_4"));

        horizontalLayout_4->addWidget(lineEdit_4);

        comboBox_4 = new QComboBox(groupBox_2);
        comboBox_4->addItem(QString());
        comboBox_4->setObjectName(QString::fromUtf8("comboBox_4"));

        horizontalLayout_4->addWidget(comboBox_4);


        verticalLayout->addLayout(horizontalLayout_4);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer);

        pushButton = new QPushButton(groupBox_2);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        horizontalLayout_5->addWidget(pushButton);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer_2);

        pushButton_2 = new QPushButton(groupBox_2);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));

        horizontalLayout_5->addWidget(pushButton_2);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer_3);


        verticalLayout->addLayout(horizontalLayout_5);


        verticalLayout_2->addWidget(groupBox_2);


        retranslateUi(MolarityCalculator);

        QMetaObject::connectSlotsByName(MolarityCalculator);
    } // setupUi

    void retranslateUi(QWidget *MolarityCalculator)
    {
        MolarityCalculator->setWindowTitle(QApplication::translate("MolarityCalculator", "\345\210\206\345\255\220\351\207\217\350\256\241\347\256\227\345\231\250", nullptr));
        groupBox_2->setTitle(QApplication::translate("MolarityCalculator", "\345\267\245\344\275\234\345\214\272", nullptr));
        label_5->setText(QApplication::translate("MolarityCalculator", "\350\264\250\351\207\217", nullptr));
        comboBox_2->setItemText(0, QApplication::translate("MolarityCalculator", "kg", nullptr));
        comboBox_2->setItemText(1, QApplication::translate("MolarityCalculator", "g", nullptr));
        comboBox_2->setItemText(2, QApplication::translate("MolarityCalculator", "mg", nullptr));
        comboBox_2->setItemText(3, QApplication::translate("MolarityCalculator", "\316\274g", nullptr));
        comboBox_2->setItemText(4, QApplication::translate("MolarityCalculator", "ng", nullptr));

        comboBox_2->setCurrentText(QApplication::translate("MolarityCalculator", "g", nullptr));
        label_2->setText(QApplication::translate("MolarityCalculator", "=", nullptr));
        label_6->setText(QApplication::translate("MolarityCalculator", "\346\265\223\345\272\246", nullptr));
        comboBox->setItemText(0, QApplication::translate("MolarityCalculator", "M", nullptr));
        comboBox->setItemText(1, QApplication::translate("MolarityCalculator", "mM", nullptr));
        comboBox->setItemText(2, QApplication::translate("MolarityCalculator", "\316\274M", nullptr));
        comboBox->setItemText(3, QApplication::translate("MolarityCalculator", "nM", nullptr));

        label_3->setText(QApplication::translate("MolarityCalculator", "X", nullptr));
        label_7->setText(QApplication::translate("MolarityCalculator", "\344\275\223\347\247\257", nullptr));
        comboBox_3->setItemText(0, QApplication::translate("MolarityCalculator", "L", nullptr));
        comboBox_3->setItemText(1, QApplication::translate("MolarityCalculator", "mL", nullptr));
        comboBox_3->setItemText(2, QApplication::translate("MolarityCalculator", "\316\274L", nullptr));
        comboBox_3->setItemText(3, QApplication::translate("MolarityCalculator", "nL", nullptr));

        comboBox_3->setCurrentText(QApplication::translate("MolarityCalculator", "mL", nullptr));
        label_4->setText(QApplication::translate("MolarityCalculator", "X", nullptr));
        label->setText(QApplication::translate("MolarityCalculator", "\347\211\251\350\264\250\345\220\215", nullptr));
        pushButton_3->setText(QApplication::translate("MolarityCalculator", "\350\256\260\345\275\225\347\211\251\350\264\250", nullptr));
        label_8->setText(QApplication::translate("MolarityCalculator", "\345\210\206\345\255\220\351\207\217", nullptr));
        comboBox_4->setItemText(0, QApplication::translate("MolarityCalculator", "g/mol", nullptr));

        pushButton->setText(QApplication::translate("MolarityCalculator", "\350\256\241\347\256\227", nullptr));
        pushButton_2->setText(QApplication::translate("MolarityCalculator", "\351\207\215\347\275\256", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MolarityCalculator: public Ui_MolarityCalculator {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MOLARITYCALCULATOR_H
