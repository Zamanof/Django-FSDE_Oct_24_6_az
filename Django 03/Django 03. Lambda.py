# Lambda expressions
# lambda params: function_body
import random


def is_even(n):
    """
    lambda x: x % 2 == 0
    """
    return n % 2 == 0


def is_negative(n):
    """
       lambda x: x < 0
    """
    return n < 0


def filter_even(n: list)->list:
    evens = []
    for i in n:
        if i % 2 == 0:
            evens.append(i)
    return evens


def filter_odd(n: list)->list:
    odds = []
    for i in n:
        if i % 2 != 0:
            odds.append(i)
    return odds


def my_filter(n: list, func)->list:
    filtered = []
    for i in n:
        if func(i):
            filtered.append(i)
    return filtered


lst = [1, 12, -34, 4, 5, -6, 73, 8, 97, 110]

# print(filter_even(lst))
# print(filter_odd(lst))
# print(my_filter(lst, lambda x: x > 0))
# print(my_filter(lst, is_negative))

# func = is_even
# print(type(lambda x: x > 0))
