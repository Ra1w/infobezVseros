import sys
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QApplication
from PyQt6.QtGui import QFont
from App.encrypt import Encrypt
from App.decrypt import Decrypt
from App.description import Description

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Стеганография в изображениях")

        self.tab = QTabWidget()
        self.tab.setFont(QFont("Times", 16))
        self.setCentralWidget(self.tab)
        self.setGeometry(200, 200, 650, 500)
        self.setStyleSheet("background-color: #828cae; color: #000000")

        self.DescriptionTab = Description()
        self.tab.addTab(self.DescriptionTab, "Описание программы")

        self.EncryptTab = Encrypt()
        self.tab.addTab(self.EncryptTab, "Шифрование")

        self.DecryptTab = Decrypt()
        self.tab.addTab(self.DecryptTab, "Расшифрование")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
