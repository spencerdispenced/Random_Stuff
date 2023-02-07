

#  https://leetcode.com/problems/longest-repeating-character-replacement/


def character_replacement_optimized(s: str, k: int) -> int:
    count = {}
    res = 0

    left = 0
    max_freq = 0  # optimization
    for right in range(len(s)):
        count[s[right]] = 1 + count.get(s[right], 0)

        # update max_freq to either current or newly added char
        max_freq = max(max_freq, count[s[right]])

        if (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        res = max(res, right - left + 1)
    return res


def character_replacement(s: str, k: int) -> int:
    # Time: O(26 * n) or O(n),
    count = {}
    res = 0
    left = 0

    for right in range(len(s)):
        # Increment count of letter
        count[s[right]] = 1 + count.get(s[right], 0)

        # check if window is valid,
        # window size (left-right + 1) - max char count
        #  is equal to the number of replacements needed, check
        #  if greater than k (invalid window)
        while (right - left + 1) - max(count.values()) > k:
            # decrement count of char at left pointer
            count[s[left]] -= 1

            # move left pointer
            left += 1

        res = max(res, right - left + 1)

    return res


if __name__ == '__main__':
    s1 = "ABAB"
    k1 = 2  # 4

    s2 = "AABABBA"
    k2 = 1  # 4

    s3 = "ABABBA"
    k3 = 2  # 5

    print(character_replacement(s1, k1))
    print(character_replacement(s2, k2))
    print(character_replacement(s3, k3))
