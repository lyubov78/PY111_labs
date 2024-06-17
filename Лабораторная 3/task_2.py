from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализовать алгоритм сортировки подсчетами
    if not container:
        return container

    max_value = max(container)
    count_arr = [0] * (max_value + 1)

    for num in container:
        count_arr[num] += 1

    sorted_arr = []
    for value, count in enumerate(count_arr):
        sorted_arr.extend([value] * count)

    return sorted_arr

if __name__ == "__main__":
    data = [1, 3, 2, 4, 0, 6, 8, 7, 9, 5, 10]
    print(sort(data))
