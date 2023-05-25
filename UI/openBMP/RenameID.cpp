#include "RenameID.h"
#include "ui_RenameID.h"

RenameID::RenameID(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::RenameID)
{
    ui->setupUi(this);
}

RenameID::~RenameID()
{
    delete ui;
}
