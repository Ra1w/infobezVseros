from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont

class Description(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: {}".format('#ffffff'))

        layout = QVBoxLayout(self)
        self.label = QLabel()
        self.label.setText("Эта программа созданна для того, чтобы уничтожить человечество!\n [злобный смех]\n\n\n\n\n\n\n\n")
        self.label.setStyleSheet("background-color: {}".format('#828cae'))
        self.label.setFont(QFont("Times", 14))
        layout.addWidget(self.label, 0)