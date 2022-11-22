

# https://leetcode.com/problems/longest-consecutive-sequence/description/

def find_max_concequtive_sequence(nums: list) -> int:
    # Time: O(n), Space O(n)
    nums_set = set(nums)

    max_sequence = 0
    for number in nums_set:
        if number - 1 not in nums_set:
            sequence = 0
            while number + sequence in nums_set:
                sequence += 1
            max_sequence = max(max_sequence, sequence)
    return max_sequence


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

    print(find_max_concequtive_sequence(nums))
    print(find_max_concequtive_sequence(nums2))
