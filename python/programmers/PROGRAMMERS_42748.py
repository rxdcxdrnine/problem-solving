from typing import List
import heapq


def solution(array, commands):
    answer: List[int] = []
    for command in commands:
        start, end, k = command

        numbers: List[int] = array[start - 1:end]
        heap: List[int] = []

        for number in numbers:
            heapq.heappush(heap, number)

        n: int = 0
        while heap:
            number = heapq.heappop(heap)
            n += 1

            if n == k:
                answer.append(number)

    return answer