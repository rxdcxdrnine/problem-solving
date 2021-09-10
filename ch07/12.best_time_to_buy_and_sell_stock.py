import sys
from typing import List


def maxProfit(prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


if __name__ == "__main__":
    prices = [7, 2, 4, 1]
    print(maxProfit(prices))
