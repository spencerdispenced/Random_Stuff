
# https://leetcode.com/problems/top-k-frequent-elements/

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    # Time: O(n+n) or just O(n)
    counts = {}
    # init list of lists in size nums
    freq = [[] for i in range(len(nums) + 1)]

    # count each occurance of number, {value: count}
    for number in nums:
        counts[number] = 1 + counts.get(number, 0)

    for number, count in counts.items():
        # at index 'frequency', insert 'value' of occurance into list
        freq[count].append(number)

    print(counts)
    print(freq)
    res = []
    # iterate through list backwards, value of highest indexes get appended first
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            # when len of result is same as top k, return
            if len(res) == k:
                return res


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(top_k_frequent(nums, k))

    nums2 = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]
    k2 = 2
    print(top_k_frequent(nums2, k2))

    nums3 = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
    k3 = 2
    print(top_k_frequent(nums3, k3))
