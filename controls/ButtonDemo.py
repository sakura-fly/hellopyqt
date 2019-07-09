import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication


class ButtonDemo(QWidget):
    def __init__(self):
        super(ButtonDemo, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Button")

        vlayout = QVBoxLayout()

        self.button1 = QPushButton('first')
        self.disable = QPushButton('disable')
        self.moren = QPushButton('默认&R')
        self.moren.setDefault(True)

        self.disable.setEnabled(False)

        self.button1.setCheckable(True)
        self.button1.toggle()

        self.button1.clicked.connect(lambda: self.whichButton(self.button1))
        self.moren.clicked.connect(lambda: self.whichButton(self.moren))
        self.button1.clicked.connect(self.buttonState)

        vlayout.addWidget(self.button1)
        vlayout.addWidget(self.disable)
        vlayout.addWidget(self.moren)
        self.setLayout(vlayout)

    def whichButton(self, btn: QPushButton):
        print("按了 " + btn.text())

    def buttonState(self):
        print(self.button1.isChecked())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ButtonDemo()
    main.show()
    sys.exit(app.exec_())
