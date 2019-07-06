import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication


class IconWindow(QMainWindow):
    def __init__(self, parent=None):
        super(IconWindow, self).__init__(parent)

        # 设置窗口标题
        self.setWindowTitle("icon mainWindow")

        #         尺寸
        self.resize(400, 300)
#         设置窗口图标
        self.setWindowIcon(QIcon('./img/uzi.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # app.setWindowIcon(QIcon('./img/uzi.png'))
    main = IconWindow()
    main.show()

    sys.exit(app.exec_())
