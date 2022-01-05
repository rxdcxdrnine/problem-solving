# leetcode 347

import collections
import heapq

def topKFrequent_A(nums, k):
    freqs = collections.Counter(nums)
    freqs_heap = []

    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))

    topk = list()
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])

if __name__ == "__main__":
    print(topKFrequent_A([1, 1, 1, 2, 2, 3], 2))