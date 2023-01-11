

# https://leetcode.com/problems/container-with-most-water/

def max_area_brute(nums):
    # Time: O(n^2)
    res = 0

    for l in range(len(nums)):
        for r in range(l + 1, len(nums)):
            area = (r - l) * min(nums[l], nums[r])
            res = max(res, area)
    return res


def most_water(nums):
    left = 0
    right = len(nums) - 1

    area = 0
    while left < right:
        width = right - left
        lowest_height = min(nums[left], nums[right])
        curr_area = width * lowest_height

        area = max(area, curr_area)

        if nums[left] < nums[right]:
            left += 1
        elif nums[right] <= nums[left]:
            right -= 1

    return area


if __name__ == '__main__':
    h1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]  # 49
    h2 = [1, 1]  # 1

    # print(max_area_brute(h1))
    # print(max_area_brute(h2))

    print(most_water(h1))
    print(most_water(h2))
