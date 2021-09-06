import collections

def removeDuplicateLetters_A(s):
    counter, stack, seen = collections.Counter(s), [], set()

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
        while stack and stack[-1] > char and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

    return ''.join(stack)

if __name__ == "__main__":
    print(removeDuplicateLetters_A("bcabc"))