#include "LigationCalculator.h"
#include "ui_LigationCalculator.h"

LigationCalculator::LigationCalculator(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::LigationCalculator)
{
    ui->setupUi(this);
}

LigationCalculator::~LigationCalculator()
{
    delete ui;
}

void LigationCalculator::on_pushButton_5_clicked()
{

}

void LigationCalculator::on_pushButton_6_clicked()
{

}
