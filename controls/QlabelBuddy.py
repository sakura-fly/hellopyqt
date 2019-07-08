import sys

from PyQt5.QtWidgets import QDial, QLabel, QLineEdit, QPushButton, QGridLayout, QApplication, QDialog


class QlabelByddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("buddy")

        nameLabel = QLabel("&Name")
        nameLineEdit = QLineEdit()

        nameLabel.setBuddy(nameLineEdit)

        pwdLabel = QLabel("&pwd")
        pwdLineEdit = QLineEdit()

        pwdLabel.setBuddy(pwdLineEdit)

        btnOk = QPushButton("&ok")
        btncancel = QPushButton("&cancel")

        layout = QGridLayout()
        layout.addWidget(nameLabel, 0, 0)
        layout.addWidget(nameLineEdit, 0, 1)
        layout.addWidget(pwdLabel, 1, 0)
        layout.addWidget(pwdLineEdit, 1, 1)
        layout.addWidget(btnOk, 2, 0)
        layout.addWidget(btncancel, 2, 1)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = QlabelByddy()
    main.show()
    sys.exit(app.exec_())


