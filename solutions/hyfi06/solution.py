"""Solution module"""
from typing import List


class Solution:
    """Class solution of challenge """

    def duplicate_zeros(self, arr: List[int]):
        """Duplicate the zeros in a list"""
        zeros = 0
        last_index = 0

        arr_len = len(arr)
        for index, item in enumerate(arr):
            if item == 0:
                if index + zeros + 1 < arr_len:
                    zeros += 1
                    last_index = index
                else:
                    break

        index = arr_len - 1

        print(f'{"="*5}{arr}:{zeros}{"="*5}')
        while zeros > 0 and index - zeros >= 0:
            print(f'{index}: {arr} zeros:  {zeros}')
            print(f'|-- {index - zeros}:{arr[index - zeros]} => {index}:{arr[index]}')
            arr[index] = arr[index - zeros]

            if arr[index - zeros] == 0 and index - zeros <= last_index:
                arr[index - 1] = 0
                zeros -= 1
                index -= 1
            index -= 1
        print(f'>: {arr}')
        print('\n\n')


def run():
    solution = Solution()
    solution.duplicate_zeros(list([0]))
    solution.duplicate_zeros(list([0, 0]))
    solution.duplicate_zeros(list([1, 0]))
    solution.duplicate_zeros(list([0, 1]))
    solution.duplicate_zeros(list([1, 1]))
    solution.duplicate_zeros(list([1, 0, 0, 0, 0]))
    solution.duplicate_zeros(list([0, 1, 1, 0, 1, 1, 1]))
    solution.duplicate_zeros(list([0, 1, 0, 0, 1, 0, 0, 3]))
    solution.duplicate_zeros(list([0, 1, 0, 1, 0, 1, 0]))
    solution.duplicate_zeros(list([0, 0, 1, 1, 1, 0, 0, 0]))
    solution.duplicate_zeros(list([0, 1, 0, 0, 1, 0, 0, 1, 0]))


if (__name__ == "__main__"):
    run()
