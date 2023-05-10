#include "LocalBlastGUI.h"
#include "ui_LocalBlastGUI.h"

LocalBlastGUI::LocalBlastGUI(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::LocalBlastGUI)
{
    ui->setupUi(this);
}

LocalBlastGUI::~LocalBlastGUI()
{
    delete ui;
}
