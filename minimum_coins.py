
def minimum_coins(target_value: int, coins: list[int]) -> int:
    """ Find minimum number of values 'coins' needed to make change 'target_value' """

    nums = [float('inf') for i in range(target_value+1)]
    nums[0] = 0

    for coin in coins:
        for amount in range(len(nums)):
            if coin <= amount:
                nums[amount] = min(nums[amount], 1 + nums[amount-coin])
    return nums[target_value]


print(minimum_coins(5, [1, 2, 3]))
