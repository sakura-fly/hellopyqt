import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication


class CenterWindow(QMainWindow):
    def __init__(self, parent=None):
        super(CenterWindow, self).__init__(parent)

        # 设置窗口标题
        self.setWindowTitle("center mainWindow")

        #         尺寸
        self.resize(800, 600)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('./img/uzi.png'))
    main = CenterWindow()
    main.show()
    sys.exit(app.exec_())
