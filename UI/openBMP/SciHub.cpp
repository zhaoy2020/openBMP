#include "SciHub.h"
#include "ui_SciHub.h"

SciHub::SciHub(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::SciHub)
{
    ui->setupUi(this);
}

SciHub::~SciHub()
{
    delete ui;
}
