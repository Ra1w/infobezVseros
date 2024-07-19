from PyQt6.QtWidgets import QTextEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, QMessageBox
from PyQt6.QtGui import QFont
from App.cipher import Blue_changing
from PIL import Image
import os

Image.MAX_IMAGE_PIXELS = 1000000000

file_path = ''

class Encrypt (QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: {}".format('#ffffff'))

        vlayout = QVBoxLayout(self)
        h1layout = QHBoxLayout(self)

        self.btn_select_file = QPushButton("Выбрать файл", self)
        self.btn_select_file.resize(100, 20)
        self.btn_select_file.setFont(QFont("Times", 16))
        vlayout.addWidget(self.btn_select_file, 0)
        self.btn_select_file.clicked.connect(self.file_selection)

        self.label_selection_file = QLabel(self)
        self.label_selection_file.setText("Файл не выбран")
        self.label_selection_file.resize(100, 20)
        self.label_selection_file.setStyleSheet("background-color: {}".format('#99a4c9'))
        self.label_selection_file.setFont(QFont("Times", 16))
        vlayout.addWidget(self.label_selection_file, 1)

        vlayout.addLayout(h1layout, 2)

        self.label_plaintext = QLabel()
        self.label_plaintext.setText("Текст: ")
        self.label_plaintext.setFont(QFont("Times", 14))
        self.label_plaintext.setStyleSheet("background-color: {}".format('#99a4c9'))
        h1layout.addWidget(self.label_plaintext, 0)

        self.plaintext = QTextEdit(self)
        self.plaintext.setFont(QFont("Times", 14))
        h1layout.addWidget(self.plaintext, 1)

        self.btn_encrypt = QPushButton()
        self.btn_encrypt.setText("Зашифровать")
        self.btn_encrypt.resize(100, 20)
        self.btn_encrypt.setFont(QFont("Times", 14))
        self.btn_encrypt.clicked.connect(self.encryption)
        vlayout.addWidget(self.btn_encrypt, 3)


    def file_selection(self):
        global file_path
        file_path = QFileDialog.getOpenFileName(
            None,
            'Выбрать изображение',
            '',
            "Image files (*.png)"
        )[0]
        if file_path != '':
            self.label_selection_file.setText("Выбран файл: {}".format(file_path[file_path.rfind("/") + 1:]))

    def encryption(self):
        global file_path
        plaintext = self.plaintext.toPlainText()
        if file_path != '':
            ves = os.stat(file_path).st_size
            if ves > 100*2**20:
                msgBox3 = QMessageBox()
                msgBox3.critical(self, "Ошибка!",
                              "Слишком большое изображение, пожалуйста, выберите изображение меньшего размера")
            else:
                if ves > 5*2*20:
                    msgBox3 = QMessageBox()
                    msgBox3.information(self, "Предупреждение",
                                        "Шифрование может занят достаточно много времени, пожалуйста, подождите.")
                image = Image.open(file_path)
                x, y = image.size
                k = 1000
                if len(plaintext)*k > x*y or x*y < k:
                    msgBox2 = QMessageBox()
                    msgBox2.warning(self, "Внимание!", "Текст слишком большой или изображение слишком мало. \n"
                                    "Для безопасности данных рекомендуется взять изображение\n"
                                    "большего размера или сократить желаемый текст.")
                else:
                    Blue_changing.encrypt(plaintext, file_path)
                    msgBox = QMessageBox()
                    msgBox.information(self, "Шифрование завершено" , "Данные успешно скрыты")
