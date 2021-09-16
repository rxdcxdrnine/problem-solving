def isValid(s: str):
    stack = []

    chars = list(s)
    pair = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    while chars:
        char = chars.pop(0)
        if char == "(" or char == "{" or char == "[":
            stack.append(char)
        if char == ")" or char == "}" or char == "]":
            if not stack or stack[-1] != pair[char]:
                return False
            else:
                stack.pop()

    if stack:
        return False
    else:
        return True


if __name__ == "__main__":
    s = "{[]}"
    print(isValid(s))
