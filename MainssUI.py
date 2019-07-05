import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from signaisolt import Ui_MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWin)
    mainWin.show()
    sys.exit(app.exec_())
