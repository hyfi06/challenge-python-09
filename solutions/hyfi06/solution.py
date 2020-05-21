from typing import List


class Solution:

    def duplicate_zeros(self, l: List[int]):
        insert = 1
        list_length = len(l)
        for index, item in enumerate(l):
            if (index >= list_length):
                break
            if (item == 0):
                if(insert):
                    l.insert(index, 0)
                insert = 1 - insert
        for _ in range(list_length,len(l)):
            l.pop()