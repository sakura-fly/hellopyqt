import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import qdMainHor

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QMainWindow()
    ui = qdMainHor.Ui_MainWindow()
    ui.setupUi(mainWin)
    mainWin.show()
    sys.exit(app.exec_())
