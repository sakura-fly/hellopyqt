'''

QLineEdit 与回显模式

功能：输入单行文本

四种回显

'''
import sys

from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QApplication


class EchoModel(QWidget):
    def __init__(self):
        super(EchoModel, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("回显")

        formLayout = QFormLayout()

        normal = QLineEdit()
        no = QLineEdit()
        pwd = QLineEdit()
        pwdEdit = QLineEdit()

        formLayout.addRow("Normal", normal)
        formLayout.addRow("no", no)
        formLayout.addRow("pwd", pwd)
        formLayout.addRow("pwdEdit", pwdEdit)

        # placeholdertext 提示
        normal.setPlaceholderText("normal")
        no.setPlaceholderText("no")
        pwd.setPlaceholderText("pwd")
        pwdEdit.setPlaceholderText("pwdEdit")

        normal.setEchoMode(QLineEdit.Normal)
        no.setEchoMode(QLineEdit.NoEcho)
        pwd.setEchoMode(QLineEdit.Password)
        pwdEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)


        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = EchoModel()
    main.show()

    sys.exit(app.exec_())