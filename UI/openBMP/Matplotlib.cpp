#include "Matplotlib.h"
#include "ui_Matplotlib.h"

Matplotlib::Matplotlib(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Matplotlib)
{
    ui->setupUi(this);
}

Matplotlib::~Matplotlib()
{
    delete ui;
}
