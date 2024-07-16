from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont

class Description(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: {}".format('#ffffff'))

        layout = QVBoxLayout(self)
        self.label = QLabel()
        self.label.setText("       Стеганография - это способ передачи или хранения информации \n"
                           "с учётом сохранения в тайне самого факта такой передачи (хранения).\n"
                            "       Данное приложение служит для реализации принципов\n"
                           "стеганографии изображений. Приложение позволяет прятать\n"
                           "текст в изображении формата *.png, а также и находить \n"
                           "такой текст в изображении.\n"
                           "Поддерживаются все символы Ascii и символы Unicode от 0400 до \n "
                           "047F (Кириллица).\n"
                           "        Для безопасности данных не рекомендуется вводить более \n"
                           "80000 символов.")
        self.label.setStyleSheet("background-color: {}".format('#828cae'))
        self.label.setFont(QFont("Times", 15))
        layout.addWidget(self.label, 0)
