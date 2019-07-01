import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建QApplaction
    app = QApplication(sys.argv)
    # 创建窗口
    w = QWidget()
    w.resize(300, 500)
    # 移动窗口
    w.move(300, 300)

    # 标题
    w.setWindowTitle("hello")
    w.show()

    # 进入程序的主循环，并通过exit确保主循环安全结束
    sys.exit(app.exec_())
