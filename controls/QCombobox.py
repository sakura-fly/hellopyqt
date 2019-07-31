'''
下拉列表
'''
import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QApplication, QPushButton


class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('下拉列表')
        # self.resize(600, 800)

        layout = QVBoxLayout()

        self.lable = QLabel("请选择")

        self.btn = QPushButton('getSelect')

        self.cb = QComboBox()
        self.cb.addItem('C')
        self.cb.addItem('Java')
        self.cb.addItem('Python')
        self.cb.addItems(['C#', 'Go', 'Ruby'])

        self.cb.currentIndexChanged.connect(self.selectChange)

        layout.addWidget(self.lable)
        layout.addWidget(self.cb)
        layout.addWidget(self.btn)

        self.btn.clicked.connect(self.clickdd)



        self.setLayout(layout)

    def selectChange(self, l):
        print(l)
        self.lable.setText(self.cb.currentText())
        self.lable.adjustSize()

        for i in range(self.cb.count()):
            print('item', str(i), '=', self.cb.itemText(i))
            print('current index', l, 'select changed', self.cb.currentText())

    def clickdd(self):
        print(self.cb.currentText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())
