#include "OpenBMP.h"
#include "ui_OpenBMP.h"

OpenBMP::OpenBMP(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::OpenBMP)
{
    ui->setupUi(this);
}

OpenBMP::~OpenBMP()
{
    delete ui;
}
