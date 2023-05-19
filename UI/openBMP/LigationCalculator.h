#ifndef LIGATIONCALCULATOR_H
#define LIGATIONCALCULATOR_H

#include <QDialog>

namespace Ui {
class LigationCalculator;
}

class LigationCalculator : public QDialog
{
    Q_OBJECT

public:
    explicit LigationCalculator(QWidget *parent = nullptr);
    ~LigationCalculator();

private slots:
    void on_pushButton_5_clicked();

    void on_pushButton_6_clicked();

private:
    Ui::LigationCalculator *ui;
};

#endif // LIGATIONCALCULATOR_H
