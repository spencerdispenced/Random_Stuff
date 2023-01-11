

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


def two_sum(nums, target):
    # Time: O(n), Space: O(1)
    left = 0
    right = len(nums) - 1

    while left < right:
        curr_sum = nums[left] + nums[right]

        if curr_sum > target:
            right -= 1
        elif curr_sum < target:
            left += 1
        else:
            return [left + 1, right + 1]


if __name__ == '__main__':
    n1 = [2, 7, 11, 15]
    t1 = 9

    n2 = [2, 3, 4]
    t2 = 6

    n3 = [-1, 0]
    t3 = -1

    n4 = [1, 3, 4, 5, 7, 10, 11]
    t4 = 9

    print(two_sum(n1, t1))
    print(two_sum(n2, t2))
    print(two_sum(n3, t3))
    print(two_sum(n4, t4))
