#include "MarkPDF.h"
#include "ui_MarkPDF.h"

MarkPDF::MarkPDF(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MarkPDF)
{
    ui->setupUi(this);
}

MarkPDF::~MarkPDF()
{
    delete ui;
}
