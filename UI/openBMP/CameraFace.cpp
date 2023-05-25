#include "CameraFace.h"
#include "ui_CameraFace.h"

CameraFace::CameraFace(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::CameraFace)
{
    ui->setupUi(this);
}

CameraFace::~CameraFace()
{
    delete ui;
}
