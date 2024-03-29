#ifndef MATPLOTLIB_H
#define MATPLOTLIB_H

#include <QMainWindow>

namespace Ui {
class Matplotlib;
}

class Matplotlib : public QMainWindow
{
    Q_OBJECT

public:
    explicit Matplotlib(QWidget *parent = nullptr);
    ~Matplotlib();

private:
    Ui::Matplotlib *ui;
};

#endif // MATPLOTLIB_H
