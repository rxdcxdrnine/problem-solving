# leetcode 5

# time limit exceeded
def longestPalindrome_(s):
    palindrome = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            letters = list(s[i:(j + 1)])

            while len(letters) > 1:
                if letters[0] == letters[-1]:
                    letters.pop()
                    letters.pop(0)
                else:
                    break

            if len(letters) == 0 or len(letters) == 1:
                palindrome.append(s[i:(j + 1)])

    return max(palindrome, key=len)


def longestPalindrome_A(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # slicing with original left pointer and original right pointer + 1
        return s[left + 1: (right - 1) + 1]

    if len(s) <= 1 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 2), expand(i, i + 3),
                     key=len)
    return result


if __name__ == "__main__":
    print(longestPalindrome_A("babad"))