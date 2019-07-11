import sys

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QRadioButton, QPushButton, QApplication


class RadioButtonDemo(QWidget):
    def __init__(self):
        super(RadioButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('radioButton')

        hLayout = QHBoxLayout()
        self.button1 = QRadioButton("11")
        self.button2 = QRadioButton("22")

        self.button1.toggled.connect(self.buttonState)
        self.button2.toggled.connect(self.buttonState)
        # print(self.button1.__doc__)

        self.button1.setChecked(True)
        # self.button1.clicked.connect(self.buttonState)
        # self.button2.clicked.connect(self.buttonState)

        hLayout.addWidget(self.button1)
        hLayout.addWidget(self.button2)
        self.setLayout(hLayout)

    def buttonState(self):
        b = self.sender()
        # if b.isChecked():
        print(b.text())
        print(b.isChecked())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = RadioButtonDemo()
    main.show()
    sys.exit(app.exec_())
