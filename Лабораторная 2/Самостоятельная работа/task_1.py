from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    ...  # TODO реализовать итеративный алгоритм бинарного поиска
    if not seq:
        raise ValueError("Ошибка! Последовательность пустая.")
    if value not in seq:
        raise ValueError("Ошибка! Элемент отсутствует.")

    left_border = 0
    right_border = len(seq) - 1

    while left_border <= right_border:
        mid_index = left_border + (right_border - left_border) // 2
        mid_value = seq[mid_index]
        if value == mid_value:
            while True:
                if not 0 <= mid_index - 1 < len(seq) or seq[mid_index - 1] != value:
                    break
                else:
                    mid_index -= 1
            return mid_index
        elif mid_value > value:
            right_border = mid_index - 1
        else:
            left_border = mid_index + 1


if __name__ == "__main__":
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(1, seq))
    print(binary_search(10, seq))
    print(binary_search(11, seq))  # ValueError
