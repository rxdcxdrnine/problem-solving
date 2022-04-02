from typing import List


def solution(M: int, truth_nums: List[int], parties: List[List[int]]):

    mask: int = 0
    for num in truth_nums:
        mask += 2 ** (num - 1)

    targets: List[int] = []
    for party_nums in parties:
        target: int = 0
        for num in party_nums:  # party_nums
            target += 2 ** (num - 1)

        targets.append(target)

    while True:
        answer = M
        flag: bool = True

        for target in targets:
            if mask & target == 0:
                continue

            answer -= 1
            if mask != mask | target:
                flag = False

            mask = mask | target

        if flag:
            break

    return answer


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    inputs: List[int] = list(map(int, input().split()))
    truth_nums = inputs[1:]

    parties: List[List[int]] = []
    for _ in range(M):
        inputs: List[int] = list(map(int, input().split()))
        parties.append(inputs[1:])

    print(solution(M, truth_nums, parties))
