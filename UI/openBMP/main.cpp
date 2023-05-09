#include "OpenBMP.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    OpenBMP w;
    w.show();

    return a.exec();
}
