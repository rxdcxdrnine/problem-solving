# leetcode 739

## time limit exceeded
def dailyTemperatures_0(T):
    days = []

    for i in range(len(T)):
        distance = 0
        for j in range(i, len(T)):
            if T[j] > T[i]:
                break
            if j == len(T) - 1:
                distance = 0
                break
            distance += 1
        days.append(distance)
    return days


def dailyTemperatures_A(T):
    answer = [0] * len(T)
    stack = []
    for i, cur in enumerate(T):
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    return answer

if __name__ == "__main__":
    print(dailyTemperatures_A([73, 74, 75, 71, 69, 72, 76, 73]))

