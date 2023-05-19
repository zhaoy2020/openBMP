#ifndef MOLARITYCALCULATOR_H
#define MOLARITYCALCULATOR_H

#include <QWidget>

namespace Ui {
class MolarityCalculator;
}

class MolarityCalculator : public QWidget
{
    Q_OBJECT

public:
    explicit MolarityCalculator(QWidget *parent = nullptr);
    ~MolarityCalculator();

private:
    Ui::MolarityCalculator *ui;
};

#endif // MOLARITYCALCULATOR_H
