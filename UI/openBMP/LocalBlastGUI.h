#ifndef LOCALBLASTGUI_H
#define LOCALBLASTGUI_H

#include <QWidget>

namespace Ui {
class LocalBlastGUI;
}

class LocalBlastGUI : public QWidget
{
    Q_OBJECT

public:
    explicit LocalBlastGUI(QWidget *parent = nullptr);
    ~LocalBlastGUI();

private slots:
    void on_pushButton_6_clicked();

    void on_pushButton_clicked();

    void on_pushButton_2_toggled(bool checked);

    void on_pushButton_4_clicked();

    void on_pushButton_5_clicked();

private:
    Ui::LocalBlastGUI *ui;
};

#endif // LOCALBLASTGUI_H
