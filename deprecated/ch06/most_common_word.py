# leetcode 819
import re
import collections

def mostCommonWord_0(paragraph, banned):
    tokens = re.findall("[a-zA-Z]+", paragraph)
    lower_tokens = map(lambda x: x.lower(), tokens)
    counter = collections.Counter(lower_tokens)

    filtered = []
    for key, value in counter.items():
        if key not in banned:
            filtered.append((key, value))
    filtered.sort(key=lambda x: x[1])

    return filtered[-1][0]


def mostCommonWord_A(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
             if word not in banned]

    counts = collections.Counter(words)
    return max(counts, key=counts.get)


if __name__ == "__main__":
    print(mostCommonWord_A("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))