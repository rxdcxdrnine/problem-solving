# leetcode 771
import collections

def numJewelsInStones_0(jewels, stones):
    count = 0
    for jewel in jewels:
        for stone in stones:
            if jewel == stone:
                count += 1

    return count


def numJewelsInStones_A(jewels, stones):
    freqs = {}
    count = 0

    for char in stones:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1

    for char in jewels:
        if char in freqs:
            count += freqs[char]

    return count


def numJewelsInStones_B(jewels, stones):
    freqs = collections.defaultdict(int)
    count = 0

    for char in stones:
        freqs[char] += 1

    for char in jewels:
        count += freqs[char]

    return count


def numJewelsInStones_C(jewels, stones):
    freqs = collections.Counter(stones)
    count = 0

    for char in jewels:
        count += freqs[char]

    return count


if __name__ == "__main__":
    J = "aA"
    S = "aAAbbbb"
    print(numJewelsInStones_A(J, S))