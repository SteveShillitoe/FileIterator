
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QStatusBar, QVBoxLayout
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Iterates through the files in a selected directory'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        verticalLayout = QVBoxLayout()
        verticalLayout.addStretch(1)
        
        self.setLayout(verticalLayout)
        self.statusbar = QStatusBar()
        self.statusbar.showMessage('Some status bar message')
        verticalLayout.addWidget(self.statusbar)
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 