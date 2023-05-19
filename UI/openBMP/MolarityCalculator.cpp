#include "MolarityCalculator.h"
#include "ui_MolarityCalculator.h"

MolarityCalculator::MolarityCalculator(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::MolarityCalculator)
{
    ui->setupUi(this);
}

MolarityCalculator::~MolarityCalculator()
{
    delete ui;
}
