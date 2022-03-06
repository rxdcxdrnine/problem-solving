import collections
from typing import Dict


def numJewelsInStones(jewels: str, stones: str) -> int:
    counter: Dict[str, int] = collections.Counter(stones)
    total_count: int = 0

    for char, count in counter.items():
        if char in jewels:
            total_count += count

    return total_count


if __name__ == "__main__":
    print(numJewelsInStones("aA", "aAAbbbb"))

