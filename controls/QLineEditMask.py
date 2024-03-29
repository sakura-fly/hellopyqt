from PyQt5.QtWidgets import *
import sys


class QLineEditMask(QWidget):
    def __init__(self):
        super(QLineEditMask, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('用掩码限制QLineEdit控件的输入')
        formLayout = QFormLayout()

        ipLineEdit = QLineEdit()
        macLineEdit = QLineEdit()
        dateLineEdit = QLineEdit()
        licenseLineEdit = QLineEdit()
        onlyReadLineEdit = QLineEdit("只读")
        onlyReadLineEdit.setReadOnly(True)
        # 192.168.21.45
        ipLineEdit.setInputMask('000.000.000.000;_')
        macLineEdit.setInputMask('HH:HH:HH:HH:HH:HH;_')
        dateLineEdit.setInputMask('0000-00-00')
        licenseLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;_')

        ipLineEdit.textChanged.connect(self.printText)
        macLineEdit.textChanged.connect(self.printText)
        dateLineEdit.textChanged.connect(self.printText)
        licenseLineEdit.textChanged.connect(self.printText)

        formLayout.addRow('数字掩码', ipLineEdit)
        formLayout.addRow('Mac掩码', macLineEdit)
        formLayout.addRow('日期掩码', dateLineEdit)
        formLayout.addRow('许可证掩码', licenseLineEdit)
        formLayout.addRow('只读', onlyReadLineEdit)

        self.setLayout(formLayout)

    def printText(self, text):
        print(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditMask()
    main.show()
    sys.exit(app.exec_())
