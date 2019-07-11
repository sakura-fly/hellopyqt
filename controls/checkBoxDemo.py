import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QApplication


class checkBoxDemo(QWidget):
    def __init__(self):
        super(checkBoxDemo, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("复选框")

        layout = QHBoxLayout()

        self.checkBox1 = QCheckBox("checkbox1")
        self.checkBox2 = QCheckBox("checkbox2")
        self.checkBox3 = QCheckBox("半选中")

        self.bs = [
            self.checkBox1,
            self.checkBox2,
            self.checkBox3
        ]

        for i in self.bs:
            i.stateChanged.connect(self.chexkBoxStat)
            layout.addWidget(i)

        self.checkBox1.setChecked(True)
        self.checkBox3.setTristate(True)
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        self.checkBox2.setCheckState(Qt.PartiallyChecked)
        self.checkBox2.setChecked(False)

        self.setLayout(layout)

    def chexkBoxStat(self):
        sender = self.sender()
        # print(sender.text() + "  " + str(sender.isChecked()) + "  " + str(sender.checkState()))
        print('----------')
        for i in self.bs:
            print(i.text() + "  " + str(i.isChecked()) + "  " + str(i.checkState()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = checkBoxDemo()
    main.show()
    sys.exit(app.exec_())
