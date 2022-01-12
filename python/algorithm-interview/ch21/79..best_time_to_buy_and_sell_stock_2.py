from typing import List


def maxProfit(prices: List[int]):
    result: int = 0
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            result += prices[i + 1] - prices[i]

    return result


if __name__ == "__main__":
    print(maxProfit([7, 1, 5, 3, 6, 4]))