#ifndef OPENBMP_H
#define OPENBMP_H

#include <QMainWindow>

namespace Ui {
class OpenBMP;
}

class OpenBMP : public QMainWindow
{
    Q_OBJECT

public:
    explicit OpenBMP(QWidget *parent = nullptr);
    ~OpenBMP();

private:
    Ui::OpenBMP *ui;
};

#endif // OPENBMP_H
