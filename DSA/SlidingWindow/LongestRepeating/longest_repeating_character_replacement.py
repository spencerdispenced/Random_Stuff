

#  https://leetcode.com/problems/longest-repeating-character-replacement/


def character_replacement(s: str, k: int) -> int:
    count = {}
    res = 0

    l = 0
    maxf = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        if (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)
    return res


if __name__ == '__main__':
    s1 = "ABAB"
    k1 = 2  # 4

    s2 = "AABABBA"
    k2 = 1  # 4

    print(character_replacement(s1, k1))
    print(character_replacement(s2, k2))
