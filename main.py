import sys

from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QTextEdit, QPushButton
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
        self.task_type_selector, self.filename_input, self.start_button = [None] * 3
        self.task_type, self.range, self.filename = None, [None, None], None
        self.init_ui()
        self.show()

    def init_ui(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle('Примеры по информатике')

        self.task_type_selector = QComboBox(self)
        self.task_type_selector.addItems(TASK_TYPES)
        self.task_type_selector.setFont(QFont('Arial', 14))
        self.task_type_selector.resize(250, 35)
        self.task_type_selector.move(100, 50)

        self.filename_input = QTextEdit('', self)
        self.filename_input.setFont(QFont('Arial', 14))
        self.filename_input.resize(300, 35)
        self.filename_input.move(100, 150)

        self.start_button = QPushButton('Создать файл с примерами', self)
        self.start_button.setFont(QFont('Arial', 14))
        self.start_button.resize(300, 35)
        self.start_button.move(100, 250)
        self.start_button.clicked.connect(self.start)

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
