"""Напишите функцию, которая проверяет является ли
число палиндромом. Число передаётся в качестве параметра. Если число палиндром нужно вернуть из функции
true, иначе false.
«Палиндром» — это число, у которого первая часть
цифр равна второй перевернутой части цифр. Например,
123321—палиндром(первая часть 123, вторая 321, которая
после переворота становится 123), 546645 — палиндром,
а 421987 — не палиндром. """

def is_palindrome(number):
    number_str = str(number)
    return number_str == number_str[::-1]

print(is_palindrome(123321))  # True
print(is_palindrome(546645))  # True
print(is_palindrome(421987))  # False
