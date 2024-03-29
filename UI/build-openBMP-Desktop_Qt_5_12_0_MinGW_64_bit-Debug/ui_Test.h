/********************************************************************************
** Form generated from reading UI file 'Test.ui'
**
** Created by: Qt User Interface Compiler version 5.12.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TEST_H
#define UI_TEST_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>

QT_BEGIN_NAMESPACE

class Ui_Test
{
public:

    void setupUi(QDialog *Test)
    {
        if (Test->objectName().isEmpty())
            Test->setObjectName(QString::fromUtf8("Test"));
        Test->resize(542, 431);

        retranslateUi(Test);

        QMetaObject::connectSlotsByName(Test);
    } // setupUi

    void retranslateUi(QDialog *Test)
    {
        Test->setWindowTitle(QApplication::translate("Test", "Dialog", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Test: public Ui_Test {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_TEST_H
