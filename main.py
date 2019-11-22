import sys
import os
from random import randint, choice

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel,\
    QComboBox, QLineEdit, QPushButton, QTextEdit
from PyQt5.Qt import QFont


HEXADECIMAL_NUMBERS = '0123456789ABCDEF'
TASK_TYPES = ('1.) ?n -> ?10', '2.) ?10 -> ?n', '3.) ?n -> ?k',
              '4.) ?2 -> ?n (по табл.)', '5.) ?n -> ?2 (по табл.)',
              '6.) ?n -> ?k (по табл.)', '7.) ?n + ?n', '8.) ?n - ?n',
              '9.) ?n * ?n')
BASES = (2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16)
TABLE_BASES = (4, 8, 16)


def to_decimal(num, base):  # функция для перевода числа в десятичную СС
    num = [HEXADECIMAL_NUMBERS.index(digit) for digit in str(num)]

    for digit in num:
        if digit >= base:
            raise ValueError('Введено число, не соответствующее заданной СС')

    return sum([num[-i - 1] * base ** i for i in range(len(num))])


def from_decimal(num, base):  # функция для перевода числа из десятичной СС
    res = []
    while num != 0:
        res.append(num % base)
        num //= base

    res = list(map(lambda d: HEXADECIMAL_NUMBERS[d], res))[::-1]
    return ''.join(res)


class InterfaceWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.task_type_label, self.task_type_selector, self.range_start_label,\
            self.range_start_input, self.range_end_label, self.range_end_input,\
            self.filename_label, self.filename_input, self.start_button,\
            self.output_console = [None] * 10
        self.task_type, self.range, self.filename = None, [0, 0], None
        self.init_ui()
        self.show()

    def init_ui(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle('Примеры по информатике')

        grid = QGridLayout()
        grid.setHorizontalSpacing(50)
        grid.setContentsMargins(50, 10, 50, 10)
        self.setLayout(grid)

        self.task_type_label = QLabel('Тип задания:', self)
        self.task_type_label.setFont(QFont('Arial', 14))
        grid.addWidget(self.task_type_label, 0, 0)

        self.task_type_selector = QComboBox(self)
        self.task_type_selector.addItems(TASK_TYPES)
        self.task_type_selector.setFont(QFont('Arial', 14))
        grid.addWidget(self.task_type_selector, 0, 1)

        self.range_start_label = QLabel('Минимальное число:', self)
        self.range_start_label.setFont(QFont('Arial', 14))
        grid.addWidget(self.range_start_label, 1, 0)

        self.range_start_input = QLineEdit('', self)
        self.range_start_input.setFont(QFont('Arial', 14))
        self.range_start_input.setMaximumHeight(35)
        grid.addWidget(self.range_start_input, 1, 1)

        self.range_end_label = QLabel('Максимальное число:', self)
        self.range_end_label.setFont(QFont('Arial', 14))
        grid.addWidget(self.range_end_label, 2, 0)

        self.range_end_input = QLineEdit('', self)
        self.range_end_input.setFont(QFont('Arial', 14))
        self.range_end_input.setMaximumHeight(35)
        grid.addWidget(self.range_end_input, 2, 1)

        self.filename_label = QLabel('Название файла:', self)
        self.filename_label.setFont(QFont('Arial', 14))
        grid.addWidget(self.filename_label, 3, 0)

        self.filename_input = QLineEdit('', self)
        self.filename_input.setFont(QFont('Arial', 14))
        self.filename_input.setMaximumHeight(35)
        grid.addWidget(self.filename_input, 3, 1)

        self.start_button = QPushButton('Создать файл с примерами', self)
        self.start_button.setFont(QFont('Arial', 14))
        self.start_button.setMinimumHeight(40)
        self.start_button.clicked.connect(self.start)
        grid.addWidget(self.start_button, 4, 0, 1, 2)

        self.output_console = QTextEdit('', self)
        self.output_console.setFont(QFont('Arial', 12))
        self.output_console.setReadOnly(True)
        self.output_console.setMaximumHeight(200)
        grid.addWidget(self.output_console, 5, 0, 1, 2)

    def start(self):
        self.task_type = self.task_type_selector.currentIndex() + 1

        try:
            self.range[0] = int(self.range_start_input.text())
            self.range[1] = int(self.range_end_input.text())
        except Exception as ex:
            self.output_console.append('Ошибка: неверный формат входных данных ({}).'.format(ex))
            return
        if self.range[0] >= self.range[1]:
            self.output_console.append('Ошибка: минимальное число диапазона больше или равно максимальному.')
            return

        self.filename = self.filename_input.text()
        if self.filename == '':
            self.output_console.append('Ошибка: имя файла не задано.')
            return
        if os.path.exists(self.filename):
            self.output_console.append('Ошибка: файл с таким именем уже существует.')
            return

        generator = NumeralSystems(self.task_type, self.range, self.filename)
        generator.variables()


class NumeralSystems:

    def __init__(self, task, ranges, file):
        self.task = task
        self.start = ranges[0]
        self.end = ranges[1]
        self.file = file

    def variables(self):
        if self.task == 1:
            self.task_1()
        elif self.task == 2:
            self.task_2()
        elif self.task == 3:
            self.task_3()
        elif self.task == 4:
            self.task_4()
        elif self.task == 5:
            self.task_5()
        elif self.task == 6:
            self.task_6()
        return True
        # self.file_writer()

    def file_writer(self, num, base1, base2, answer):
        with open(self.file+'.txt', 'a', encoding='utf-8') as f:
            f.write(':: Вопрос \n:: \\( %s_\{%s\} = ?_\{%s\} \\)\t{=%s}\n:: В ответе укажите только число (без указания основания).'
                    '\n\n' % (num, base1, base2, answer))

    def task_1(self):
        for num in range(self.start, self.end + 1):
            base = choice(BASES)
            num_n = from_decimal(num, base)
            self.file_writer(num_n, base, 10, num)

    def task_2(self):
        for num in range(self.start, self.end + 1):
            base = choice(BASES)
            num_n = to_decimal(num, base)
            self.file_writer(num_n, 10, base, num)

    def task_3(self):
        for num in range(self.start, self.end + 1):
            from_base = choice(BASES)
            to_base = choice(BASES)
            if from_base == to_base:
                continue
            num_k = from_decimal(num, to_base)
            num_n = from_decimal(num, from_base)
            self.file_writer(num_n, from_base, to_base, num_k)

    def task_4(self):
        for num in range(self.start, self.end + 1):
            base = choice(TABLE_BASES)
            num_2 = from_decimal(num, 2)
            num_n = from_decimal(num, base)
            self.file_writer(num_2, 2, base, num_n)

    def task_5(self):
        for num in range(self.start, self.end + 1):
            base = choice(TABLE_BASES)
            num_2 = from_decimal(num, 2)
            num_n = from_decimal(num, base)
            self.file_writer(num_n, base, 2, num_2)

    def task_6(self):
        for num in range(self.start, self.end + 1):
            from_base = choice(TABLE_BASES)
            to_base = choice(TABLE_BASES)
            if from_base == to_base:
                continue
            num_k = from_decimal(num, to_base)
            num_n = from_decimal(num, from_base)
            self.file_writer(num_n, from_base, to_base, num_k)

    def task_7(self):
        pass

    def task_8(self):
        pass

    def task_9(self):
        pass


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        gui = InterfaceWidget()
        sys.exit(app.exec())
    except Exception as e:
        print('Ошибка:', e)
