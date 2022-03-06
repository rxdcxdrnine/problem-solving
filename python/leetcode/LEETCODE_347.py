import collections
import heapq
from typing import List, Dict, Tuple


def topKFrequent(nums: List[int], k: int) -> List[int]:

    counter: Dict[int, int] = collections.Counter(nums)
    heap: List[Tuple[int, int]] = []
    result: List[int] = []

    for num, count in counter.items():
        heapq.heappush(heap, (-count, num))

    while k:
        count, num = heapq.heappop(heap)
        result.append(num)
        k -= 1

    return result


if __name__ == "__main__":
    print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
