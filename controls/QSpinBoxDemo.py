import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSpinBox


class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('计数器')

        layout = QVBoxLayout()
        self.label = QLabel('当前数')
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        self.setLayout(layout)

        self.spinbox = QSpinBox()
        layout.addWidget(self.spinbox)
        self.spinbox.valueChanged.connect(self.valueChange)

    def valueChange(self):
        self.label.setText('当前值' + str(self.sender().value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSpinBoxDemo()
    main.show()
    sys.exit(app.exec_())
