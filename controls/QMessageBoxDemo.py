"""
1、关于对话框
2、错误对话框
3、警告对话框
4、提问对话框
5、消息对话框

2点差异

1  对话框图片不同
2  按钮不同
"""
import sys

from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QPushButton, QApplication, QMainWindow, QWidget


class QMessageBoxDemo(QWidget):
    def __init__(self):
        super(QMessageBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("qMessageBoxDemo")
        self.resize(500, 500)

        vLayout = QVBoxLayout()

        self.button1 = QPushButton("关于对话框")
        self.button2 = QPushButton("错误对话框")
        self.button3 = QPushButton("警告对话框")
        self.button4 = QPushButton("提问对话框")
        self.button5 = QPushButton("消息对话框")

        self.button1.clicked.connect(self.showDialog)
        self.button2.clicked.connect(self.showDialog)
        self.button3.clicked.connect(self.showDialog)
        self.button4.clicked.connect(self.showDialog)
        self.button5.clicked.connect(self.showDialog)
        vLayout.addWidget(self.button1)
        vLayout.addWidget(self.button2)
        vLayout.addWidget(self.button3)
        vLayout.addWidget(self.button4)
        vLayout.addWidget(self.button5)

        self.setLayout(vLayout)

    def showDialog(self):
        # print(233)
        text = self.sender().text()
        if text == "关于对话框":
            QMessageBox.about(self, '关于', '这是一个关于对话框')
        elif text == "消息对话框":
            reply = QMessageBox.information(self, 'info', '消息对话框', QMessageBox.Yes, QMessageBox.No)
            print(reply == QMessageBox.Yes)
        elif text == "错误对话框":
            QMessageBox.critical(self, '错误', '这是一个  错误  对话框')
        elif text == "提问对话框":
            QMessageBox.question(self, '提问', '这是一个  提问  对话框')
        elif text == "警告对话框":
            QMessageBox.warning(self, '警告', '这是一个  警告  对话框', QMessageBox.Yes, QMessageBox.No)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QMessageBoxDemo()
    main.show()
    sys.exit(app.exec_())
