import heapq
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        max_digit = 0
        for num in nums:
            max_digit = max(max_digit, len(str(num)))
        max_digit += 2

        heap = []
        for num in nums:
            concat = str(num)

            if len(str(num)) < max_digit:
                while len(concat) < max_digit:
                    concat += str(num)
                concat = concat[:max_digit]

            heapq.heappush(heap, (-int(concat), str(num)))

        answer = ""
        while heap:
            element = heapq.heappop(heap)
            answer += element[1]

        if int(answer) == 0:
            return "0"

        return answer
