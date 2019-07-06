import sys

from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QHBoxLayout, QWidget


class QuitApp(QMainWindow):
    def __init__(self):
        super(QuitApp, self).__init__()

        self.resize(800, 600)
        self.setWindowTitle("quit app")

        # add button
        self.button = QPushButton("quit")

        # 将按钮的点击  信号  和  槽  绑定
        self.button.clicked.connect(self.onClick)

        hLayOut = QHBoxLayout()
        hLayOut.addWidget(self.button)

        rootFrame = QWidget()
        rootFrame.setLayout(hLayOut)

        self.setCentralWidget(rootFrame)

    def onClick(self):
        """
        按钮单击事件
        :return:
        """
        # 获取事件对象
        sender = self.sender()
        print(sender.text() + " press")
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApp()
    main.show()

    sys.exit(app.exec_())
