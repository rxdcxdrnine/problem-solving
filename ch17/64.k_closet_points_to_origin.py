import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def euclidean_dist(p1, p2):
            return math.sqrt(math.pow((p1[0] - p2[0]), 2) + math.pow((p1[1] - p2[1]), 2))

        heap = []
        center = [0, 0]

        for point in points:
            heapq.heappush(heap, (euclidean_dist(center, point), point))

        n = 0
        result = []

        while heap:
            _, point = heapq.heappop(heap)
            print(point)
            n += 1

            if n <= k:
                result.append(point)

        return result
