# leetcode 121
import sys

# time limit exceeded
def maxProfit_0(prices):
    result = 0
    for i in range(len(prices)):
        if prices[:i + 1] and prices[i:] \
                and max(prices[i:]) - min(prices[:i + 1]) > result:
            result = max(prices[i:]) - min(prices[:i + 1])
    return result


def maxProfit_A(prices):
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return price


if __name__ == "__main__":
    print(maxProfit_A([2, 1, 2, 0, 1]))