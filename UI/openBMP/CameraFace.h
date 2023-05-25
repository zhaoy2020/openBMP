#ifndef CAMERAFACE_H
#define CAMERAFACE_H

#include <QDialog>

namespace Ui {
class CameraFace;
}

class CameraFace : public QDialog
{
    Q_OBJECT

public:
    explicit CameraFace(QWidget *parent = nullptr);
    ~CameraFace();

private:
    Ui::CameraFace *ui;
};

#endif // CAMERAFACE_H
