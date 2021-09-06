def longestPalindrome(s: str) -> str:
    result = ''

    if len(s) < 2 or s == s[::-1]:
        return s

    for ind in range(len(s) - 1):
        odd_left, odd_right = ind, ind + 1
        even_left, even_right = ind, ind + 2

        # check when palindrome's length is odd
        while odd_left >= 0 and odd_right <= len(s) and s[odd_left] == s[odd_right - 1]:
            odd_left -= 1
            odd_right += 1
        odd = s[odd_left + 1: odd_right - 1]

        # check when palindrome's length is even
        while even_left >= 0 and even_right <= len(s) and s[even_left] == s[even_right - 1]:
            even_left -= 1
            even_right += 1
        even = s[even_left + 1: even_right - 1]

        result = max(result, odd, even, key=len)

    return result


if __name__ == "__main__":
    s = "a"
    print(longestPalindrome(s))
