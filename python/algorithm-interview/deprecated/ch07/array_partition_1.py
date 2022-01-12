# leetcode 561

def arrayPairSum_A(nums):
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


def arrayPairSum_B(nums):
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n

    return sum


def arrayPairSum_C(nums):
    return sum(sorted(nums)[::2])


if __name__ == "__main__":
    print(arrayPairSum_A([6,2,6,5,1,2]))