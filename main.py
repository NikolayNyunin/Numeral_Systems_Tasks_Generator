import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


HEXADECIMAL_NUMBERS = '0123456789ABCDEF'


def to_decimal(num, base):  # функция для перевода числа в десятичную СС
    num = [HEXADECIMAL_NUMBERS.index(digit) for digit in str(num)]
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
        self.start_button = None
        self.task_type, self.range, self.filename = None, [None, None], None
        self.init_ui()
        self.show()

    def init_ui(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle('Примеры по информатике')

        self.start_button = QPushButton('Создать файл с примерами')
        self.start_button.clicked.connect(self.start)

    def start(self):
        generator = NumeralSystems(self.task_type, self.range[0],
                                   self.range[1], self.filename)
        generator.start()


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
