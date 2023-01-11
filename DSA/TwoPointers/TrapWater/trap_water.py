

# https://leetcode.com/problems/trapping-rain-water/


def trap_water(height):
    # Time: O(n), Space: O(1)

    if not height:
        return 0

    left = 0
    right = len(height) - 1
    left_max = height[left]
    right_max = height[right]

    total = 0

    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, height[left])
            total += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            total += right_max - height[right]

    return total


if __name__ == '__main__':
    h1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # 6
    h2 = [4, 2, 0, 3, 2, 5]  # 9

    print(trap_water(h1))
    print(trap_water(h2))
