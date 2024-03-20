"""Напишите функцию, которая принимает два числа
в качестве параметра и отображает все четные числа
между ними."""

def display_even_numbers(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number)

display_even_numbers(1, 10)
