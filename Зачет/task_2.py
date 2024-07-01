# 2. Задача консенсуса DNA рядов

from typing import Iterable


def dna_chains(data: Iterable[str]) -> str:

    length = len(data[0])
    consensus = ""

    for i in range(length):

        count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

        for string in data:
            count[string[i]] += 1
        most_common = max(count, key=count.get)  # Самый часто встречаемый
        consensus += most_common

    return consensus


if __name__ == '__main__':

    data = [
        'ATTA',
        'ACTA',
        'AGCA',
        'ACAA',
        'ACTA'
    ]
    print(dna_chains(data))  # 'ACTA'
