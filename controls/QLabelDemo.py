import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtWidgets import QMainWindow, QLabel, QHBoxLayout, QApplication, QVBoxLayout, QWidget


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText('<font color=red>text</font>')
        # 背景色
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)  # 设置背景色
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText('<a href="#">link</a>')

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('pic')
        # label3.setPixmap(QPixmap('./img/logo.png'))

        label4.setText('<a href="www.github.com">github</a>')
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('link')
        # true打开浏览器false触发事件
        label4.setOpenExternalLinks(True)

        vLayout = QVBoxLayout()

        vLayout.addWidget(label1)
        vLayout.addWidget(label2)
        vLayout.addWidget(label3)
        vLayout.addWidget(label4)

        label2.linkHovered.connect(self.hover)
        label4.linkActivated.connect(self.clicked)

        self.setLayout(vLayout)

        self.setWindowTitle("Label show")
        # self.resize(400, 300)

    def hover(self):
        print('hover 2')

    def clicked(self):
        print("click 4")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # app.setWindowIcon(QIcon('./img/uzi.png'))
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())
