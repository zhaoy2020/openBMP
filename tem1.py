import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Simple GUI')
        
        layout = QVBoxLayout()
        label = QLabel('Hello, PyQt5!')
        layout.addWidget(label)

        button = QPushButton('Click Me!')
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button)

        self.setLayout(layout)
        self.show()

    def on_button_clicked(self):
        print('Button clicked!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
