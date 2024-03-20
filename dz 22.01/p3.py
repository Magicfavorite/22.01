"""Напишите функцию, которая отображает пустой или
заполненный квадрат из некоторого символа. Функция
принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
■ если она равна True, квадрат заполненный;
■ если False, квадрат пустой."""


def display_square(side_length, symbol, filled):
    if filled:
        for i in range(side_length):
            for j in range(side_length):
                print(symbol, end='')
            print()
    else:
        for i in range(side_length):
            print(' '  *  side_length)

display_square(5, '%', True)
