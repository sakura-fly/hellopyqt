import sys

from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton, QHBoxLayout, QApplication, QVBoxLayout


class QTextEidtDemo(QWidget):
    def __init__(self):
        super(QTextEidtDemo, self).__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()

        self.setTextBtn = QPushButton('set text')
        self.getTextBtn = QPushButton('get text')
        self.setHtmlBtn = QPushButton('set html')
        self.sethtmlByTextBtn = QPushButton('set html by html')
        self.gethrmlBtn = QPushButton('get html')

        vLayout = QVBoxLayout()
        vLayout.addWidget(self.textEdit)
        vLayout.addWidget(self.setTextBtn)
        vLayout.addWidget(self.getTextBtn)
        vLayout.addWidget(self.setHtmlBtn)
        vLayout.addWidget(self.gethrmlBtn)
        vLayout.addWidget(self.sethtmlByTextBtn)

        self.setTextBtn.clicked.connect(self.setText)
        self.getTextBtn.clicked.connect(self.getText)
        self.setHtmlBtn.clicked.connect(self.setHtml)
        self.gethrmlBtn.clicked.connect(self.getHtml)
        self.sethtmlByTextBtn.clicked.connect(self.sethtmlByText)

        self.setLayout(vLayout)

    def setText(self):
        self.textEdit.setText("233")

    def getText(self):
        print(self.textEdit.toPlainText())

    def setHtml(self):
        self.textEdit.setHtml("<b>233</b>")

    def sethtmlByText(self):
        self.textEdit.setText("<b>233</b>")

    def getHtml(self):
        print(self.textEdit.toHtml())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTextEidtDemo()
    main.show()
    sys.exit(app.exec_())

