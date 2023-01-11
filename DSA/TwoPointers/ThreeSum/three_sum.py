

# https://leetcode.com/problems/3sum/

def three_sum(nums):
    # 3 numbers from array that sum to 0
    # Time: O(nlogn) for sort, O(n^2) for traversal -> O(n^2)
    # Space: O(1) or O(n) depending on sort library
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:  # not first value and not same as value before
            continue

        # Solve twoSum
        left = i + 1
        right = len(nums) - 1

        while left < right:
            curr_sum = a + nums[left] + nums[right]

            if curr_sum > 0:
                right -= 1
            elif curr_sum < 0:
                left += 1
            else:
                res.append([a, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return res


if __name__ == '__main__':
    nums1 = [-1, 0, 1, 2, -1, -4]  # [[-1,-1,2],[-1,0,1]]

    nums2 = [0, 1, 1]  # []

    nums3 = [0, 0, 0]  # [[0,0,0]]

    nums4 = [-3, 3, 4, -3, 1, 2]  # [[-3, 1, 2]]

    print(three_sum(nums1))
    print(three_sum(nums2))
    print(three_sum(nums3))
    print(three_sum(nums4))
