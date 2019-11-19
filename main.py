import sys

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel,\
    QComboBox, QTextEdit, QPushButton, QPlainTextEdit
from PyQt5.Qt import QFont


HEXADECIMAL_NUMBERS = '0123456789ABCDEF'
TASK_TYPES = ('1.) ?n -> ?10', '2.) ?10 -> ?n', '3.) ?n -> ?k',
              '4.) ?2 -> ?n (по табл.)', '5.) ?n -> ?2 (по табл.)',
              '6.) ?n -> ?k (по табл.)', '7.) ?n + ?n', '8.) ?n - ?n',
              '9.) ?n * ?n')


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
        self.task_type, self.range, self.filename = None, [None, None], None
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

        self.range_start_input = QTextEdit('', self)
        self.range_start_input.setFont(QFont('Arial', 14))
        self.range_start_input.setMaximumHeight(35)
        grid.addWidget(self.range_start_input, 1, 1)

        self.range_end_label = QLabel('Максимальное число:', self)
        self.range_end_label.setFont(QFont('Arial', 14))
        grid.addWidget(self.range_end_label, 2, 0)

        self.range_end_input = QTextEdit('', self)
        self.range_end_input.setFont(QFont('Arial', 14))
        self.range_end_input.setMaximumHeight(35)
        grid.addWidget(self.range_end_input, 2, 1)

        self.filename_label = QLabel('Название файла:', self)
        self.filename_label.setFont(QFont('Arial', 14))
        grid.addWidget(self.filename_label, 3, 0)

        self.filename_input = QTextEdit('', self)
        self.filename_input.setFont(QFont('Arial', 14))
        self.filename_input.setMaximumHeight(35)
        grid.addWidget(self.filename_input, 3, 1)

        self.start_button = QPushButton('Создать файл с примерами', self)
        self.start_button.setFont(QFont('Arial', 14))
        self.start_button.setMinimumHeight(40)
        self.start_button.clicked.connect(self.start)
        grid.addWidget(self.start_button, 4, 0, 1, 2)

        self.output_console = QPlainTextEdit('', self)
        self.output_console.setFont(QFont('Arial', 14))
        self.output_console.setReadOnly(True)
        self.output_console.setMaximumHeight(200)
        grid.addWidget(self.output_console, 5, 0, 1, 2)

    def start(self):
        generator = NumeralSystems(self.task_type, self.range, self.filename)
        generator.variables()


class NumeralSystems:

    def __init__(self, task, ranges, file):
        self.task = task
        self.start = ranges[0]
        self.end = ranges[1]
        self.file = file

    def variables(self):
        pass


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        gui = InterfaceWidget()
        sys.exit(app.exec())
    except Exception as e:
        print('Ошибка:', e)
