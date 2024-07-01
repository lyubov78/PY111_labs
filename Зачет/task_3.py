# 3. Аренда ракет

from typing import Iterable, List, Tuple


def rocket_rental(rent: Iterable[Tuple[int, int]]) -> bool:

    rent = list(rent)

    for start, end in rent:
        if start < 0 or start >= 24 or end <= 0 or end > 24 or start >= end:
            raise ValueError("Недопустимый интервал времени!")

    rent.sort(key=lambda x: x[0])  # Сортируем интервалы по времени начала

    for i in range(1, len(rent)):
        if rent[i][0] < rent[i - 1][1]:  # Если начало нового интервала меньше времени окончания предыдущего интервала
            return False

    return True


if __name__ == '__main__':

    rent_1 = [(1, 5), (6, 7), (22, 24), (7, 13), (15, 20)]
    rent_2 = [(13, 15), (15, 20), (18, 23)]
    rent_3 = [(12, 13), (5, 6)]

    print(rocket_rental(rent_1))  # True
    print(rocket_rental(rent_2))  # False
    print(rocket_rental(rent_3))  # True
