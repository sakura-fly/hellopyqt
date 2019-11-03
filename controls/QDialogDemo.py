"""
对话框:QDialog

QMessageBox对话框
QColorDialog颜色
QFileDialog文件
QFontDialog字体
QInputDialog输入
"""
import sys

from PyQt5 import Qt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QDialog, QApplication


class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QDialogDemo")
        self.resize(300, 300)

        self.button = QPushButton(self)
        self.button.setText("弹出对话框")
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()
        closeBtn = QPushButton("close", dialog)
        closeBtn.clicked.connect(dialog.close)
        dialog.setWindowTitle("this is a dialog")
        dialog.resize(200, 200)
        dialog.setWindowModality(Qt.ApplicationModal)

        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()
    sys.exit(app.exec_())
