def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    ...  # TODO реализовать итеративный алгоритм нахождения факториала
    if not isinstance(n, int):
        raise TypeError("Ошибка! Значение должно целым числом.")
    if n < 0:
        raise ValueError("Ошибка! Значение должно быть положительным.")
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    print(factorial_iterative(5))
    print(factorial_iterative(0))
    print(factorial_iterative(1))
    print(factorial_iterative(-1))  # ValueError
    print(factorial_iterative(1.5))  # ValueError
    print(factorial_iterative("1"))  # TypeError
