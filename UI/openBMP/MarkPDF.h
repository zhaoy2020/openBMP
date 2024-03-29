#ifndef MARKPDF_H
#define MARKPDF_H

#include <QMainWindow>

namespace Ui {
class MarkPDF;
}

class MarkPDF : public QMainWindow
{
    Q_OBJECT

public:
    explicit MarkPDF(QWidget *parent = nullptr);
    ~MarkPDF();

private:
    Ui::MarkPDF *ui;
};

#endif // MARKPDF_H
