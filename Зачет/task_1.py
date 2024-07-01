# 1. Считалочка

def counting_rhyme(n: list, k: int) -> int:

    index = 0  # Начало считалочки

    # Пока не останется последний человек
    while len(n) > 1:
        index = (index + k - 1) % len(n)
        n.pop(index)

    return n[0]  # Последний оставшийся человек


if __name__ == '__main__':
    n = [1, 2, 3, 4, 5, 6, 7]    # Количество человек
    k = 3                        # Слогов считалочки
    print(counting_rhyme(n, k))  # 4
