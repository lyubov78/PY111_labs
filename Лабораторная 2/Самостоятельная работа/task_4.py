from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    data = [target - elem for elem in nums]  #[7, 2, -2, -6]
    for i, v in enumerate(nums):
        if v in data and data.index(v) != i:
            return [i, data.index(v)]


if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))
