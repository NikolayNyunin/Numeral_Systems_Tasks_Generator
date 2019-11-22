HEXADECIMAL_NUMBERS = '0123456789ABCDEF'


def type_1(num, base):  # функция для перевода числа в десятичную СС
    num = [HEXADECIMAL_NUMBERS.index(digit) for digit in str(num)]

    for digit in num:
        if digit >= base:
            raise ValueError('Введено число, не соответствующее заданной СС')

    return sum([num[-i - 1] * base ** i for i in range(len(num))])


def type_2(num, base):  # функция для перевода числа из десятичной СС
    res = []
    while num != 0:
        res.append(num % base)
        num //= base

    return ''.join(list(map(lambda d: HEXADECIMAL_NUMBERS[d], res))[::-1])


def type_3(num, from_base, to_base):
    # first convert to decimal number
    num = [HEXADECIMAL_NUMBERS.index(digit) for digit in str(num)]
    n_10 = sum([num[-i - 1] * from_base ** i for i in range(len(num))])
    # now convert decimal to 'to_base' base
    res = []
    while n_10 != 0:
        res.append(n_10 % to_base)
        n_10 //= to_base

    return ''.join(list(map(lambda d: HEXADECIMAL_NUMBERS[d], res))[::-1])


print(type_3(14, 7, 2))


def type_4(num, to_base):
    # first convert to decimal number
    num = [HEXADECIMAL_NUMBERS.index(digit) for digit in str(num)]
    n_10 = sum([num[-i - 1] * 2 ** i for i in range(len(num))])
    # now convert decimal to 'to_base' base
    res = []
    while n_10 != 0:
        res.append(n_10 % to_base)
        n_10 //= to_base
    return ''.join(list(map(lambda d: HEXADECIMAL_NUMBERS[d], res))[::-1])


def type_5(num, from_base):
    # first convert to decimal number
    num = [HEXADECIMAL_NUMBERS.index(digit) for digit in str(num)]
    n_10 = sum([num[-i - 1] * from_base ** i for i in range(len(num))])
    # now convert decimal to 'to_base' base
    res = []
    while n_10 != 0:
        res.append(n_10 % 2)
        n_10 //= 2

    return ''.join(list(map(lambda d: HEXADECIMAL_NUMBERS[d], res))[::-1])


def type_6():
    pass  # то же что и 3


def type_7(num1, num2, base):
    num1 = [HEXADECIMAL_NUMBERS.index(digit) for digit in str(num1)]
    n_1_10 = sum([num1[-i - 1] * base ** i for i in range(len(num1))])
    # перевод первого числа в десятичную сс
    num2 = [HEXADECIMAL_NUMBERS.index(digit) for digit in str(num2)]
    n_2_10 = sum([num2[-i - 1] * base ** i for i in range(len(num2))])
    # перевод второго числа в десятичную сс
    result = n_1_10 + n_2_10
    res = []
    while result != 0:
        res.append(result % base)
        result //= base

    return ''.join(list(map(lambda d: HEXADECIMAL_NUMBERS[d], res))[::-1])


def type_8(num1, num2, base):
    num1 = [HEXADECIMAL_NUMBERS.index(digit) for digit in str(num1)]
    n_1_10 = sum([num1[-i - 1] * base ** i for i in range(len(num1))])
    # перевод первого числа в десятичную сс
    num2 = [HEXADECIMAL_NUMBERS.index(digit) for digit in str(num2)]
    n_2_10 = sum([num2[-i - 1] * base ** i for i in range(len(num2))])
    # перевод второго числа в десятичную сс
    result = n_1_10 - n_2_10
    res = []
    while result != 0:
        res.append(result % base)
        result //= base

    return ''.join(list(map(lambda d: HEXADECIMAL_NUMBERS[d], res))[::-1])


def type_9(num1, num2, base):
    num1 = [HEXADECIMAL_NUMBERS.index(digit) for digit in str(num1)]
    n_1_10 = sum([num1[-i - 1] * base ** i for i in range(len(num1))])
    # перевод первого числа в десятичную сс
    num2 = [HEXADECIMAL_NUMBERS.index(digit) for digit in str(num2)]
    n_2_10 = sum([num2[-i - 1] * base ** i for i in range(len(num2))])
    # перевод второго числа в десятичную сс
    result = n_1_10 * n_2_10
    res = []
    while result != 0:
        res.append(result % base)
        result //= base

    return ''.join(list(map(lambda d: HEXADECIMAL_NUMBERS[d], res))[::-1])


