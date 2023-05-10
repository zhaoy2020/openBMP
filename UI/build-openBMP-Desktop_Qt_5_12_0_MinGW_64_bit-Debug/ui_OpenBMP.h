/********************************************************************************
** Form generated from reading UI file 'OpenBMP.ui'
**
** Created by: Qt User Interface Compiler version 5.12.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_OPENBMP_H
#define UI_OPENBMP_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_OpenBMP
{
public:
    QAction *actionAboout;
    QAction *actionUpdate;
    QAction *actionLocal_Blast_GUI;
    QAction *actionExit;
    QWidget *centralWidget;
    QVBoxLayout *verticalLayout;
    QFrame *frame;
    QVBoxLayout *verticalLayout_2;
    QLabel *label;
    QFrame *frame_2;
    QHBoxLayout *horizontalLayout;
    QPushButton *pushButton;
    QPushButton *pushButton_2;
    QLabel *label_2;
    QMenuBar *menuBar;
    QMenu *menuBlast;
    QMenu *menuGO;
    QMenu *menuKEGG;
    QMenu *menuCOG;
    QMenu *menuOthers;
    QMenu *menuGames;
    QMenu *menuHelp;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *OpenBMP)
    {
        if (OpenBMP->objectName().isEmpty())
            OpenBMP->setObjectName(QString::fromUtf8("OpenBMP"));
        OpenBMP->resize(464, 407);
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/icons/images/bacteria.svg"), QSize(), QIcon::Normal, QIcon::On);
        OpenBMP->setWindowIcon(icon);
        actionAboout = new QAction(OpenBMP);
        actionAboout->setObjectName(QString::fromUtf8("actionAboout"));
        actionUpdate = new QAction(OpenBMP);
        actionUpdate->setObjectName(QString::fromUtf8("actionUpdate"));
        actionLocal_Blast_GUI = new QAction(OpenBMP);
        actionLocal_Blast_GUI->setObjectName(QString::fromUtf8("actionLocal_Blast_GUI"));
        actionExit = new QAction(OpenBMP);
        actionExit->setObjectName(QString::fromUtf8("actionExit"));
        centralWidget = new QWidget(OpenBMP);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(centralWidget->sizePolicy().hasHeightForWidth());
        centralWidget->setSizePolicy(sizePolicy);
        verticalLayout = new QVBoxLayout(centralWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        frame = new QFrame(centralWidget);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setEnabled(true);
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(frame->sizePolicy().hasHeightForWidth());
        frame->setSizePolicy(sizePolicy1);
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        verticalLayout_2 = new QVBoxLayout(frame);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        label = new QLabel(frame);
        label->setObjectName(QString::fromUtf8("label"));

        verticalLayout_2->addWidget(label);


        verticalLayout->addWidget(frame);

        frame_2 = new QFrame(centralWidget);
        frame_2->setObjectName(QString::fromUtf8("frame_2"));
        sizePolicy1.setHeightForWidth(frame_2->sizePolicy().hasHeightForWidth());
        frame_2->setSizePolicy(sizePolicy1);
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        horizontalLayout = new QHBoxLayout(frame_2);
        horizontalLayout->setSpacing(6);
        horizontalLayout->setContentsMargins(11, 11, 11, 11);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        pushButton = new QPushButton(frame_2);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        QSizePolicy sizePolicy2(QSizePolicy::Maximum, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(pushButton->sizePolicy().hasHeightForWidth());
        pushButton->setSizePolicy(sizePolicy2);
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/icons/images/Update.svg"), QSize(), QIcon::Normal, QIcon::On);
        pushButton->setIcon(icon1);

        horizontalLayout->addWidget(pushButton);

        pushButton_2 = new QPushButton(frame_2);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));
        sizePolicy2.setHeightForWidth(pushButton_2->sizePolicy().hasHeightForWidth());
        pushButton_2->setSizePolicy(sizePolicy2);
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/icons/images/citation.svg"), QSize(), QIcon::Normal, QIcon::On);
        pushButton_2->setIcon(icon2);
        pushButton_2->setAutoDefault(false);

        horizontalLayout->addWidget(pushButton_2);

        label_2 = new QLabel(frame_2);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setAlignment(Qt::AlignCenter);
        label_2->setTextInteractionFlags(Qt::LinksAccessibleByMouse);

        horizontalLayout->addWidget(label_2);


        verticalLayout->addWidget(frame_2);

        OpenBMP->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(OpenBMP);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 464, 17));
        menuBlast = new QMenu(menuBar);
        menuBlast->setObjectName(QString::fromUtf8("menuBlast"));
        menuGO = new QMenu(menuBar);
        menuGO->setObjectName(QString::fromUtf8("menuGO"));
        menuKEGG = new QMenu(menuBar);
        menuKEGG->setObjectName(QString::fromUtf8("menuKEGG"));
        menuCOG = new QMenu(menuBar);
        menuCOG->setObjectName(QString::fromUtf8("menuCOG"));
        menuOthers = new QMenu(menuBar);
        menuOthers->setObjectName(QString::fromUtf8("menuOthers"));
        menuGames = new QMenu(menuBar);
        menuGames->setObjectName(QString::fromUtf8("menuGames"));
        menuHelp = new QMenu(menuBar);
        menuHelp->setObjectName(QString::fromUtf8("menuHelp"));
        OpenBMP->setMenuBar(menuBar);
        mainToolBar = new QToolBar(OpenBMP);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        OpenBMP->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(OpenBMP);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        OpenBMP->setStatusBar(statusBar);

        menuBar->addAction(menuBlast->menuAction());
        menuBar->addAction(menuGO->menuAction());
        menuBar->addAction(menuKEGG->menuAction());
        menuBar->addAction(menuCOG->menuAction());
        menuBar->addAction(menuOthers->menuAction());
        menuBar->addAction(menuGames->menuAction());
        menuBar->addAction(menuHelp->menuAction());
        menuBlast->addAction(actionLocal_Blast_GUI);
        menuBlast->addAction(actionExit);
        menuHelp->addAction(actionUpdate);

        retranslateUi(OpenBMP);

        QMetaObject::connectSlotsByName(OpenBMP);
    } // setupUi

    void retranslateUi(QMainWindow *OpenBMP)
    {
        OpenBMP->setWindowTitle(QApplication::translate("OpenBMP", "OpenBMP", nullptr));
        actionAboout->setText(QApplication::translate("OpenBMP", "Aboout", nullptr));
        actionUpdate->setText(QApplication::translate("OpenBMP", "About", nullptr));
        actionLocal_Blast_GUI->setText(QApplication::translate("OpenBMP", "Local Blast GUI", nullptr));
        actionExit->setText(QApplication::translate("OpenBMP", "Exit", nullptr));
        label->setText(QApplication::translate("OpenBMP", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">\345\214\227\345\233\275\351\243\216\345\205\211\357\274\214\345\215\203\351\207\214\345\206\260\345\260\201\357\274\214\344\270\207\351\207\214\351\233\252\351\243\230\343\200\202</span></p><p align=\"center\"><span style=\" font-size:14pt;\">\346\234\233\351\225\277\345\237\216\345\206\205\345\244\226\357\274\214\346\203\237\344\275\231\350\216\275\350\216\275\357\274\233</span></p><p align=\"center\"><span style=\" font-size:14pt;\">\345\244\247\346\262\263\344\270\212\344\270\213\357\274\214\351\241\277\345\244\261\346\273\224\346\273\224\343\200\202</span></p><p align=\"center\"><span style=\" font-size:14pt;\">\345\261\261\350\210\236\351\223\266\350\233\207\357\274\214\345\216\237\351\251\260\350\234\241\350\261\241\357\274\214\346\254\262\344\270\216\345\244\251\345\205\254\350\257\225\346\257\224\351\253\230\343\200\202</span></p><p align=\"center\"><span style=\" font-size:14pt;\">\351\241\273\346\231\264\346\227\245\357\274\214\347"
                        "\234\213\347\272\242\350\243\205\347\264\240\350\243\271\357\274\214\345\210\206\345\244\226\345\246\226\345\250\206\343\200\202</span></p><p align=\"center\"><span style=\" font-size:14pt;\">\346\261\237\345\261\261\345\246\202\346\255\244\345\244\232\345\250\207\357\274\214\345\274\225\346\227\240\346\225\260\350\213\261\351\233\204\347\253\236\346\212\230\350\205\260\343\200\202</span></p><p align=\"center\"><span style=\" font-size:14pt;\">\346\203\234\347\247\246\347\232\207\346\261\211\346\255\246\357\274\214\347\225\245\350\276\223\346\226\207\351\207\207\357\274\233</span></p><p align=\"center\"><span style=\" font-size:14pt;\">\345\224\220\345\256\227\345\256\213\347\245\226\357\274\214\347\250\215\351\200\212\351\243\216\351\252\232\343\200\202</span></p><p align=\"center\"><span style=\" font-size:14pt;\">\344\270\200\344\273\243\345\244\251\351\252\204\357\274\214\346\210\220\345\220\211\346\200\235\346\261\227\357\274\214\345\217\252\350\257\206\345\274\257\345\274\223\345\260\204\345\244\247\351\233"
                        "\225\343\200\202</span></p><p align=\"center\"><span style=\" font-size:14pt;\">\344\277\261\345\276\200\347\237\243\357\274\214\346\225\260\351\243\216\346\265\201\344\272\272\347\211\251\357\274\214\350\277\230\347\234\213\344\273\212\346\234\235\343\200\202</span></p><p align=\"center\"><span style=\" font-size:14pt;\">--\346\257\233\346\263\275\344\270\234</span></p></body></html>", nullptr));
        pushButton->setText(QApplication::translate("OpenBMP", "update", nullptr));
        pushButton_2->setText(QApplication::translate("OpenBMP", "citation", nullptr));
        label_2->setText(QApplication::translate("OpenBMP", "<html><head/><body><p><a href=\"https://github.com/zhaoy2020/openBMP\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/zhaoy2020/openBMP</span></a></p></body></html>", nullptr));
        menuBlast->setTitle(QApplication::translate("OpenBMP", "Blast", nullptr));
        menuGO->setTitle(QApplication::translate("OpenBMP", "GO", nullptr));
        menuKEGG->setTitle(QApplication::translate("OpenBMP", "KEGG", nullptr));
        menuCOG->setTitle(QApplication::translate("OpenBMP", "COG", nullptr));
        menuOthers->setTitle(QApplication::translate("OpenBMP", "Others", nullptr));
        menuGames->setTitle(QApplication::translate("OpenBMP", "Games", nullptr));
        menuHelp->setTitle(QApplication::translate("OpenBMP", "Help", nullptr));
    } // retranslateUi

};

namespace Ui {
    class OpenBMP: public Ui_OpenBMP {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_OPENBMP_H