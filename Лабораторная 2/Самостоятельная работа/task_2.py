from typing import Union
from itertools import count
from math import factorial


DELTA = 0.000001


def sinx(x: Union[int, float]) -> float:
    """
    Вычисление sin(x) с помощью разложения в ряд Тейлора

    :param x: x значение в радианах
    :return: значение sin(x)
    """
    ...  # TODO вычислить sin(x) с помощью разложения сумму бесконечного ряда
    result = 0
    elem = x
    ind = 1

    while abs(elem) > DELTA:
        result += elem
        elem *= -x ** 2 / ((2 * ind) * (2 * ind + 1))
        ind += 1

    return result


if __name__ == "__main__":
    print(sinx(0))
    print(sinx(1))
    print(sinx(5))
    print(sinx(15))
