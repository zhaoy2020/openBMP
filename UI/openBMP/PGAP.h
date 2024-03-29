#ifndef PGAP_H
#define PGAP_H

#include <QMainWindow>

namespace Ui {
class PGAP;
}

class PGAP : public QMainWindow
{
    Q_OBJECT

public:
    explicit PGAP(QWidget *parent = nullptr);
    ~PGAP();

private:
    Ui::PGAP *ui;
};

#endif // PGAP_H
