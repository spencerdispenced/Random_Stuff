

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    # Time: O(n+n) or just O(n)
    counts = {}
    # init list of lists in size nums
    freq = [[] for i in range(len(nums) + 1)]

    # count each occurance of number, {value: count}
    for number in nums:
        counts[number] = 1 + counts.get(number, 0)

    for count, value in counts.items():
        # at index 'value', insert frequency of occurance into list
        freq[value].append(count)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    print(top_k_frequent(nums, k))
