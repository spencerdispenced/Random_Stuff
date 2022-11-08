
from collections import defaultdict


def group_anagrams(strs):
    # Time: O(m * n)

    # mapping charCount to list of Anagrams
    res = defaultdict(list)

    for word in strs:
        # create list for each letter in alphabet
        count = [0] * 26

        # map letter to respective index, increment count of each letter
        # ascii is in order, 81 - 80 = 1, or index 1 for 'b'
        for char in word:
            count[ord(char) - ord('a')] += 1

        # add word as value corresponding to key with exact letter count
        res[tuple(count)].append(word)

    return res.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


if __name__ == '__main__':
    print(group_anagrams(strs))
