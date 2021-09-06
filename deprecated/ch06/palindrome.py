# leetcode 124
import collections
import re

def isPalindrome_0(s: str) -> bool:
    alphabet = [char.lower() for char in s if char.isalnum()]
    for i in range(len(alphabet)):
        if alphabet[i] != alphabet[(len(alphabet) - 1) - i]:
            return False
    return True


def isPalindrome_A(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # check if panlindrome
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False


def isPalindrome_B(s: str) -> bool:
    # declare deque
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


def isPalindrome_C(s: str) -> bool:
    s = s.lower()
    # filtering with regular expression
    s = re.sub("[^a-z0-9]", '', s)

    return s == s[::-1]


if __name__ == "__main__":
    print(isPalindrome_0("A man, a plan, a canal: Panama"))