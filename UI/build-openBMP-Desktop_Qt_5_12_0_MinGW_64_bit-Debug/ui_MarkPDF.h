/********************************************************************************
** Form generated from reading UI file 'MarkPDF.ui'
**
** Created by: Qt User Interface Compiler version 5.12.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MARKPDF_H
#define UI_MARKPDF_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MarkPDF
{
public:
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout_3;
    QFrame *frame;
    QVBoxLayout *verticalLayout;
    QGroupBox *groupBox;
    QVBoxLayout *verticalLayout_2;
    QTextBrowser *textBrowser;
    QPushButton *pushButton_4;
    QGroupBox *groupBox_2;
    QGridLayout *gridLayout;
    QLabel *label_2;
    QLineEdit *lineEdit_2;
    QPushButton *pushButton_2;
    QLabel *label_3;
    QLineEdit *lineEdit_3;
    QPushButton *pushButton_3;
    QLabel *label;
    QTextEdit *textEdit;
    QPushButton *pushButton;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MarkPDF)
    {
        if (MarkPDF->objectName().isEmpty())
            MarkPDF->setObjectName(QString::fromUtf8("MarkPDF"));
        MarkPDF->resize(395, 304);
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/icons/images/bacteria.svg"), QSize(), QIcon::Normal, QIcon::On);
        MarkPDF->setWindowIcon(icon);
        centralwidget = new QWidget(MarkPDF);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        verticalLayout_3 = new QVBoxLayout(centralwidget);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        frame = new QFrame(centralwidget);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        verticalLayout = new QVBoxLayout(frame);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        groupBox = new QGroupBox(frame);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        verticalLayout_2 = new QVBoxLayout(groupBox);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        textBrowser = new QTextBrowser(groupBox);
        textBrowser->setObjectName(QString::fromUtf8("textBrowser"));

        verticalLayout_2->addWidget(textBrowser);

        pushButton_4 = new QPushButton(groupBox);
        pushButton_4->setObjectName(QString::fromUtf8("pushButton_4"));

        verticalLayout_2->addWidget(pushButton_4);


        verticalLayout->addWidget(groupBox);


        verticalLayout_3->addWidget(frame);

        groupBox_2 = new QGroupBox(centralwidget);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        gridLayout = new QGridLayout(groupBox_2);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label_2 = new QLabel(groupBox_2);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout->addWidget(label_2, 0, 0, 1, 1);

        lineEdit_2 = new QLineEdit(groupBox_2);
        lineEdit_2->setObjectName(QString::fromUtf8("lineEdit_2"));

        gridLayout->addWidget(lineEdit_2, 0, 1, 1, 1);

        pushButton_2 = new QPushButton(groupBox_2);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));

        gridLayout->addWidget(pushButton_2, 0, 2, 1, 1);

        label_3 = new QLabel(groupBox_2);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout->addWidget(label_3, 1, 0, 1, 1);

        lineEdit_3 = new QLineEdit(groupBox_2);
        lineEdit_3->setObjectName(QString::fromUtf8("lineEdit_3"));

        gridLayout->addWidget(lineEdit_3, 1, 1, 1, 1);

        pushButton_3 = new QPushButton(groupBox_2);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));

        gridLayout->addWidget(pushButton_3, 1, 2, 1, 1);

        label = new QLabel(groupBox_2);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout->addWidget(label, 2, 0, 1, 1);

        textEdit = new QTextEdit(groupBox_2);
        textEdit->setObjectName(QString::fromUtf8("textEdit"));

        gridLayout->addWidget(textEdit, 2, 1, 1, 1);

        pushButton = new QPushButton(groupBox_2);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        gridLayout->addWidget(pushButton, 2, 2, 1, 1);


        verticalLayout_3->addWidget(groupBox_2);

        MarkPDF->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MarkPDF);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 395, 17));
        MarkPDF->setMenuBar(menubar);
        statusbar = new QStatusBar(MarkPDF);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MarkPDF->setStatusBar(statusbar);

        retranslateUi(MarkPDF);

        QMetaObject::connectSlotsByName(MarkPDF);
    } // setupUi

    void retranslateUi(QMainWindow *MarkPDF)
    {
        MarkPDF->setWindowTitle(QApplication::translate("MarkPDF", "MarkPDF by Zhaoy", nullptr));
        groupBox->setTitle(QApplication::translate("MarkPDF", "Sci-Hub toolkit:", nullptr));
        textBrowser->setHtml(QApplication::translate("MarkPDF", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Download papers according to DOI/PMID/Title from sci-hub/PubMed websites.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Configure the location where to save the file and the associated configuration information, before performing a batch download.</span></p></body></html>", nullptr));
        pushButton_4->setText(QApplication::translate("MarkPDF", "Open sci-hub", nullptr));
        groupBox_2->setTitle(QApplication::translate("MarkPDF", "Batch hightlight key words within PDF:", nullptr));
        label_2->setText(QApplication::translate("MarkPDF", "RawPDF(Input):", nullptr));
        lineEdit_2->setText(QApplication::translate("MarkPDF", "./RawPDF", nullptr));
        pushButton_2->setText(QApplication::translate("MarkPDF", "Open dir.", nullptr));
        label_3->setText(QApplication::translate("MarkPDF", "MatchPDF(Output):", nullptr));
        lineEdit_3->setText(QApplication::translate("MarkPDF", "./MatchPDf", nullptr));
        pushButton_3->setText(QApplication::translate("MarkPDF", "Choose dir.", nullptr));
        label->setText(QApplication::translate("MarkPDF", "Query key words:", nullptr));
        textEdit->setHtml(QApplication::translate("MarkPDF", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">cdG;cyclic di-GMP;c-diGMP;PDE;DGC</span></p></body></html>", nullptr));
        pushButton->setText(QApplication::translate("MarkPDF", "Start", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MarkPDF: public Ui_MarkPDF {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MARKPDF_H
