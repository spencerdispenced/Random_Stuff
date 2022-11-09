

def valid_anagram(s, t):
    # Time: O(s + t)
    # Space: O(s + t)

    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)

    # if count_s == count_t:
    #     return True
    # else:
    #     return False

    for c in count_s:
        if count_s[c] != count_t.get(c, 0):
            return False

    return True


if __name__ == '__main__':
    test1 = 'anagram'
    test2 = 'nagaram'
    test3 = 'apple'
    test4 = 'ppale'
    test5 = 'apple'
    test6 = 'ppalx'
    print(valid_anagram(test1, test2))
    print(valid_anagram(test3, test4))
    print(valid_anagram(test5, test6))
