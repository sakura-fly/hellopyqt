import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QApplication


class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUI()

    def initUI(self):
        formLayout = QFormLayout()
        intLine = QLineEdit()
        doubletLine = QLineEdit()
        validatortLine = QLineEdit()

        formLayout.addRow("int", intLine)
        formLayout.addRow("double", doubletLine)
        formLayout.addRow("字母数字", validatortLine)

        # int validator
        intValidator = QIntValidator()
        intValidator.setRange(1, 99)

        # 浮点，小数点后两位
        doubleValidator = QDoubleValidator()
        doubleValidator.setRange(1, 99)
        # doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        # 精度，小数点两位
        doubleValidator.setDecimals(2)
        # 数字字符
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator()
        validator.setRegExp(reg)

        intLine.setValidator(intValidator)
        doubletLine.setValidator(doubleValidator)
        validatortLine.setValidator(validator)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()

    sys.exit(app.exec_())
