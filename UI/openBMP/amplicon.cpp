#include "amplicon.h"
#include "ui_amplicon.h"

amplicon::amplicon(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::amplicon)
{
    ui->setupUi(this);
}

amplicon::~amplicon()
{
    delete ui;
}
