# leetcode 20

def isValid_A(s):
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0


if __name__ == "__main__":
    print(isValid_A("()[]{}"))