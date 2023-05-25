#ifndef RENAMEID_H
#define RENAMEID_H

#include <QDialog>

namespace Ui {
class RenameID;
}

class RenameID : public QDialog
{
    Q_OBJECT

public:
    explicit RenameID(QWidget *parent = nullptr);
    ~RenameID();

private:
    Ui::RenameID *ui;
};

#endif // RENAMEID_H
