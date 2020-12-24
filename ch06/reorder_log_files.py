# leetcode 937

def reorderLogFiles_0(logs):
    alphas = []
    nums = []

    for ind, log in enumerate(logs):
        # split log with whitespace
        split = list(''.join(log.split(' ')[1:]))
        # check if log consists of alphabet
        is_alpha = any([char.isalpha() for char in split])
        if is_alpha:
            alphas.append((log, ind))
        else:
            nums.append((log, ind))

    # sort alphas and nums with each sorting rule
    alphas.sort(key=lambda x: (x[0].split(' ')[1:], x[0].split(' ')[0]))

    concat = alphas + nums
    # sort logs with new order
    result = [logs[ind] for _, ind in concat]

    return result


def reorderLogFiles_A(logs):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x:(x.split()[1:], x.split()[0]))
    return letters + digits


if __name__ == "__main__":
    print(reorderLogFiles_A(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))