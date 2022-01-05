from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:

    answer = [0] * len(temperatures)
    stack = []

    for i, cur in enumerate(temperatures):
        while stack and cur > temperatures[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    return answer


if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures(temperatures))
