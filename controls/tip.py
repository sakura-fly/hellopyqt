import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QToolTip, QApplication, QPushButton, QHBoxLayout, QMainWindow


class Tip(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("weiruanyahei", 12))
        self.setToolTip('我好<b>开心</b>')
        self.resize(300, 400)
        self.setWindowTitle("tips")

        self.button = QPushButton('233')
        self.button.setToolTip("233")

        layout = QHBoxLayout()
        layout.addWidget(self.button)

        root = QWidget()
        root.setLayout(layout)

        self.setCentralWidget(root)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # app.setWindowIcon(QIcon('./img/uzi.png'))
    main = Tip()
    main.show()
    sys.exit(app.exec_())
