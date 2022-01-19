from typing import List
import re

def solution(s):
    answer: str = ""
    tokens: List[str] = re.split(r'(\s+)', s)

    for token in tokens:
        string: str = ""

        for ind, char in enumerate(token):
            transformed: str = char

            if ind % 2 == 0 and ord("a") <= ord(char) <= ord("z"):
                transformed = chr(ord(char) - ord("a") + ord("A"));

            if ind % 2 == 1 and ord("A") <= ord(char) <= ord("Z"):
                transformed = chr(ord(char) - ord("A") + ord("a"))

            string += transformed

        answer += string

    return answer


if __name__ == "__main__":
    s: str = " try hello world"
    print(solution(s))