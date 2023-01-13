

# https://leetcode.com/problems/longest-substring-without-repeating-characters/


def longest_substring(s: str) -> int:
    # Time: O(n), Space: O(n)
    chars = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in chars:
            chars.remove(s[l])
            l += 1
        chars.add(s[r])
        res = max(res, len(chars))
    return res


if __name__ == '__main__':
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"

    print(longest_substring(s1))
    print(longest_substring(s2))
    print(longest_substring(s3))
