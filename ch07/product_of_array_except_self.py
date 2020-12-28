# leetcode 238

def productExceptSelf_A(nums):
    out = []
    p = 1
    for i in range(0, len(nums), 1):
        out.append(p)
        p = p * nums[i]

    p = 1
    for i in range(len(nums) - 1, -1, -1):
        out[i] = out[i] * p
        p = p * nums[i]

    return out


if __name__ == "__main__":
    print(productExceptSelf_A([1, 2, 3, 4]))
