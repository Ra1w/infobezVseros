from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont

class Description(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: {}".format('#ffffff'))

        layout = QVBoxLayout(self)
        self.label = QLabel()
        self.label.setText("     Стеганография - это способ передачи или хранения информации с учётом \n"
                           "сохранения в тайне самого факта такой передачи (хранения).\n"
                            "       Данное приложение служит для реализации принципов стеганографии изображений\n"
                           "Приложение позволяет прятать текст в изображении формата *.png, а также \n"
                           "и находить такой текст в изображении.")
        self.label.setStyleSheet("background-color: {}".format('#828cae'))
        self.label.setFont(QFont("Times", 14))
        layout.addWidget(self.label, 0)
