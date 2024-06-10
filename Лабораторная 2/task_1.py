"""
This module implements some functions based on linear search algo
"""
from typing import List
import random


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    ...  # TODO реализовать итеративный линейный поиск
    if not arr:
        raise ValueError('Ошибка! Массив пустой.')
    if not isinstance(arr, list):
        raise TypeError('Ошибка! Массив не является списком.')

    index = 0
    for i in range(len(arr)):
        if arr[i] < arr[index]:
            index = i
    return index


if __name__ == "__main__":
    arr = [random.randint(1, 100) for i in range(10)]
    print(arr)
    print(f'Индекс минимального значения в списке равен {min_search(arr)}')
