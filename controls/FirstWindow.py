import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication


class FirstMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(FirstMainWindow, self).__init__(parent)

        # 设置窗口标题
        self.setWindowTitle("first mainWindow")

        #         尺寸
        self.resize(400, 300)
        self.status = self.statusBar()

        self.status.showMessage('only 5s', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('./img/uzi.png'))
    main = FirstMainWindow()
    main.show()


    sys.exit(app.exec_())
