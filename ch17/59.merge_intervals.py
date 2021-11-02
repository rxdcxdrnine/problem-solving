import collections
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        deque = collections.deque(intervals)
        result = []

        while deque:
            left = deque.popleft()
            if deque:
                right = deque.popleft()

                if left[1] >= right[0]:
                    deque.appendleft([min(left[0], right[0]), max(left[1], right[1])])
                else:
                    result.append(left)
                    deque.appendleft(right)
            else:
                result.append(left)

        return result
    