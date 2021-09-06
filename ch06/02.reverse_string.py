from typing import List


def reverseString(s: List[str]) -> None:
    s.reverse()


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    reverseString(s)
    print(s)

