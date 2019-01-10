
import sys
import os
import time
import json
from PyQt5.QtWidgets import QApplication, QWidget, QStatusBar, QVBoxLayout, \
                           QPushButton, QFileDialog, QProgressBar

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Iterates through the files in a selected directory'
        self.left = 100
        self.top = 100
        self.width = 1000
        self.height = 480
        self.directory = ""
        self.initUI()
        
    def initUI(self):
        with open('config.json') as json_data_file:
            data = json.load(json_data_file)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        verticalLayout = QVBoxLayout()
        self.setLayout(verticalLayout)

        button1Label = data['button1']
        button2Label = data['button2']

        self.btnSelectFile = QPushButton(button1Label)
        self.btnSelectFile.clicked.connect(self.OpenFile)
        verticalLayout.addWidget(self.btnSelectFile)

        self.btnShowDirectory = QPushButton(button2Label)
        self.btnShowDirectory.clicked.connect(self.IterateFiles)
        verticalLayout.addWidget(self.btnShowDirectory)

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.pbar.hide()
        verticalLayout.addWidget(self.pbar)

        verticalLayout.addStretch(1)
        
        self.statusbar = QStatusBar()
        verticalLayout.addWidget(self.statusbar)

        self.show()

    def OpenFile(self):
        fullFilePath, _ = QFileDialog.getOpenFileName(parent=self, 
                         caption="Select csv file", directory='C:\TRISTAN Data\PreClinical', filter="*.csv")
        self.directory, fileName = os.path.split(fullFilePath)
        self.statusbar.showMessage('File {} selected in directory {}.'.format(fileName, self.directory))

    def IterateFiles(self):
        self.pbar.show()
        #Create a list of csv files in the selected directory
        csvFiles = [file for file in os.listdir(self.directory) if file.lower().endswith('.csv')]
        numCSVFiles = len(csvFiles)
        self.statusbar.showMessage('The selected directory is {} with {} csv files.'
                                   .format(self.directory, str(numCSVFiles)))
        
        self.pbar.setMaximum(numCSVFiles)
        self.pbar.setValue(0)
        count = 0
        for file in csvFiles:
            count += 1
            time.sleep(1)
            self.pbar.setValue(count)
            self.statusbar.showMessage("Processing {}".format(str(file)))

        self.statusbar.showMessage("Processing complete.")
        self.pbar.hide()





 

 
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 