# 4. Сорт

# Выбран метод сортировки подсчетом, тк имеем большое кол-во часто повторяемых элементов в небольшом диапазоне.
# Сложность O(n + k) , где k - диапазон целых чисел

import random


def counting_sort(arr):

    min_value = 13
    max_value = 25
    count = [0] * (max_value - min_value + 1)

    for number in arr:  # Считаем количество каждого числа в исходном массиве
        count[number - min_value] += 1

    sorted_arr = []
    for i in range(len(count)):  # Сортируем массив
        sorted_arr.extend([i + min_value] * count[i])

    return sorted_arr


if __name__ == '__main__':

    arr = [random.randint(13, 25) for _ in range(10 ** 6)]
    print(counting_sort(arr)[:10])  # Первые 10 элементов отсортированного массива
