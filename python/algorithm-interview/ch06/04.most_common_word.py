from collections import Counter, defaultdict
from typing import List
import re

def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    splits = list(filter(lambda x: len(x) > 0, re.split("[\s!?',;.]+", paragraph.lower())))
    counter = Counter(splits)

    for word in banned:
        if counter[word]:
            counter.pop(word)

    rev_counter = defaultdict(list)
    max_val = 0
    for key, val in counter.items():
        rev_counter[val].append(key)
        if max_val < val:
            max_val = val

    return rev_counter[max_val][0]


if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(mostCommonWord(paragraph, []))
