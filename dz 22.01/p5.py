"""Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона
передаются в качестве параметров. Если границы диапанижняя граница), их нужно поменять местами."""


def product_of_range(start, end):
    if start > end:
        start, end = end, start
    product = 1
    for i in range(start, end + 1):
        product  *= i
    return product

print(product_of_range(1, 10))
