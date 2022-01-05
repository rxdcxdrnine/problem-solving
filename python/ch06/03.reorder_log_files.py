from typing import List, Dict


def reorderLogFiles(logs: List[str]) -> List[str]:
    letters, digits = [], []

    for log in logs:
        splits = log.split(' ')
        identifier = splits.pop(0)

        if splits[0].isalpha():
            letters.append([identifier, ' '.join(splits)])
        else:
            digits.append([identifier, ' '.join(splits)])

    letters.sort(key=lambda x: [x[1], x[0]])

    return [key + " " + val for key, val in letters] + \
           [key + " " + val for key, val in digits]


if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(reorderLogFiles(logs))
