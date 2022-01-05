def isPalindrome(s: str) -> bool:
    s = [char.lower() for char in s if char.isalnum()]
    return s == s[::-1]


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))
