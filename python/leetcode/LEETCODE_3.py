import collections
from typing import Dict


def lengthOfLongestSubstring(s: str) -> int:

    max_len: int = 0

    for ind in range(len(s)):
        max_len = max(move(s, ind, ind), move(s, ind, ind + 1), max_len)

    return max_len


def move(s: str, start: int, end: int):
    left, right = start, end

    counts: Dict[str, int] = collections.defaultdict(int)

    if left < 0 or right >= len(s):
        return 0

    if left != right and s[left] == s[right]:
        return 1

    counts[s[left]] += 1
    counts[s[right]] += 1

    while left > 0 and right < len(s) - 1 \
            and not counts[s[left - 1]] and not counts[s[right + 1]] and s[left - 1] != s[right + 1]:

        counts[s[left - 1]] += 1
        counts[s[right + 1]] += 1

        left -= 1
        right += 1

    return right - left + 1


if __name__ == "__main__":
    print(lengthOfLongestSubstring("pwwkew"))
