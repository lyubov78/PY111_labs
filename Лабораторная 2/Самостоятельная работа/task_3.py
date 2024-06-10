from typing import List


def reverse_string(s: List[str]) -> None:
    for i in range(len(s)//2):
        s[i], s[-1 - i] = s[-1 - i], s[i]


if __name__ == "__main__":
    s = ["1", "2", "3", "4", "5"]
    reverse_string(s)
    print(s)
