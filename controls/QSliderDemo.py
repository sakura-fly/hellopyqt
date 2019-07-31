import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSlider, QApplication


class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('滑块')

        layout = QVBoxLayout()
        self.label = QLabel('hello')
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        self.silder = QSlider(Qt.Horizontal)
        self.silder.setMinimum(10)
        self.silder.setMaximum(50)

        # 步长
        self.silder.setSingleStep(3)
        self.silder.setValue(22)

        # 刻度，在下方
        self.silder.setTickPosition(QSlider.TicksBelow)
        # 刻度间隔
        self.silder.setTickInterval(3)
        self.silder.valueChanged.connect(self.valueChange)

        layout.addWidget(self.silder)
        self.setLayout(layout)
        self.label.setFont(QFont('Arial', self.silder.value()))

    def valueChange(self):
        print('当前', self.sender().value())
        self.label.setFont(QFont('Arial', self.sender().value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()
    sys.exit(app.exec_())
