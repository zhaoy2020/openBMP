#include "PGAP.h"
#include "ui_PGAP.h"

PGAP::PGAP(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::PGAP)
{
    ui->setupUi(this);
}

PGAP::~PGAP()
{
    delete ui;
}
