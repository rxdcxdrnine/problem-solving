def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    result = [0, 0, 0]

    for i, answer in enumerate(answers):

        for j, person in enumerate([first, second, third]):
            ind = i % len(person)

            if answers[i] == person[ind]:
                result[j] += 1

    people = []
    max_val = max(result)
    for ind, num in enumerate(result):
        if num == max_val:
            people.append(ind + 1)

    return people


if __name__ == "__main__":
    answers = [3, 3, 1, 1, 1, 1, 2, 3, 4, 5]
    print(solution(answers))