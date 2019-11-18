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


class NumeralSystems:

    def __init__(self, task, start, end, file):
        self.task = task
        self.start = start
        self.end = end
        self.file = file

    def task_type(self):
        pass  # обработка self.task

    def values(self):
        pass  # обработка self.start и self.end (random)

    def file_name(self):
        pass  # обработка self.file (os?)


def main():
    pass


if __name__ == '__main__':
    main()
