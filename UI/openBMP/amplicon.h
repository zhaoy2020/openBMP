#ifndef AMPLICON_H
#define AMPLICON_H

#include <QMainWindow>

namespace Ui {
class amplicon;
}

class amplicon : public QMainWindow
{
    Q_OBJECT

public:
    explicit amplicon(QWidget *parent = nullptr);
    ~amplicon();

private:
    Ui::amplicon *ui;
};

#endif // AMPLICON_H
