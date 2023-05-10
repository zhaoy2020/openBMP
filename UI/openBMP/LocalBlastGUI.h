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

private:
    Ui::LocalBlastGUI *ui;
};

#endif // LOCALBLASTGUI_H
