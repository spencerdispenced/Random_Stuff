

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


def max_profit(prices: list[int]) -> int:
    left = 0
    right = 1
    max_profit = 0

    while right < len(prices):
        if prices[left] >= prices[right]:
            left = right
            right += 1
        else:
            max_profit = max(max_profit, prices[right] - prices[left])
            right += 1

    return max_profit


if __name__ == '__main__':
    prices1 = [7, 1, 5, 3, 6, 4]  # 5
    prices2 = [7, 6, 4, 3, 1]  # 0
    prices3 = [7, 9, 3, 5, 2, 8]  # 6
    prices4 = [3, 6, 5, 10, 1, 5, 10]  # 9
    print(max_profit(prices1))
    print(max_profit(prices2))
    print(max_profit(prices3))
    print(max_profit(prices4))
