# leetcode 42

def trap_0(height):
    result = 0
    for i in range(len(height)):
        left_max = max(height[:i + 1])
        right_max = max(height[i:])

        result += min(left_max, right_max) - height[i]

    return result


def trap_A(height):
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume


def trap_B(height):
    stack = []
    volume = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if not len(stack):
                break

        distance = i - stack[-1] - 1
        waters = min(height[i], height[stack[-1]]) - height[top]

        volume += distance * waters
        stack.append()

    return volume


if __name__ == "__main__":
    print(trap_0([4, 2, 0, 3, 2, 5]))