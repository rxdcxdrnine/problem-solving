from collections import Counter

def removeDuplicateLetters(s: str) -> str:
    counter, seen, stack = Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        if char in seen:
            pass
        else:
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

    return ''.join(stack)


if __name__ == "__main__":
    s = "bcabc"
    print(removeDuplicateLetters(s))
