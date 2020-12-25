# save for later

def sequential_argmax(nums):
    nums_dict = {ind: num for ind, num in enumerate(nums)}
    result = []

    while nums_dict:
        max_value = max(nums_dict.values())
        argmax = []

        for ind, num in nums_dict.items():
            if num == max_value:
                argmax.append(ind)
        result.append(argmax)

        for ind in sorted(argmax, reverse=True):
            del nums_dict[ind]

    return result