#ifndef SCIHUB_H
#define SCIHUB_H

#include <QMainWindow>

namespace Ui {
class SciHub;
}

class SciHub : public QMainWindow
{
    Q_OBJECT

public:
    explicit SciHub(QWidget *parent = nullptr);
    ~SciHub();

private:
    Ui::SciHub *ui;
};

#endif // SCIHUB_H
