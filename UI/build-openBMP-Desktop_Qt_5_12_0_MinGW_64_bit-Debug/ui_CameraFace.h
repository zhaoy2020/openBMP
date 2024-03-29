/********************************************************************************
** Form generated from reading UI file 'CameraFace.ui'
**
** Created by: Qt User Interface Compiler version 5.12.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CAMERAFACE_H
#define UI_CAMERAFACE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>

QT_BEGIN_NAMESPACE

class Ui_CameraFace
{
public:

    void setupUi(QDialog *CameraFace)
    {
        if (CameraFace->objectName().isEmpty())
            CameraFace->setObjectName(QString::fromUtf8("CameraFace"));
        CameraFace->resize(400, 300);

        retranslateUi(CameraFace);

        QMetaObject::connectSlotsByName(CameraFace);
    } // setupUi

    void retranslateUi(QDialog *CameraFace)
    {
        CameraFace->setWindowTitle(QApplication::translate("CameraFace", "Dialog", nullptr));
    } // retranslateUi

};

namespace Ui {
    class CameraFace: public Ui_CameraFace {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CAMERAFACE_H
