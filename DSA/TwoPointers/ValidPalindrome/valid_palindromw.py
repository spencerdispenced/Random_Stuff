

# https://leetcode.com/problems/valid-palindrome/

def is_palindrome(str):
    new_str = ''

    for c in str:
        if c.isalnum():
            new_str += c.lower()

    return new_str == new_str[::-1]


def is_palindrome_two(str):
    # Time: O(n), Space: O(1)
    left = 0
    right = len(str)-1

    while left < right:
        # increment from each side until an alphanumeric character
        while left < right and not alphaNum(str[left]):
            left += 1
        while right > left and not alphaNum(str[right]):
            right -= 1

        # Check if character on either side matches
        if str[left].lower() != str[right].lower():
            return False

        left += 1
        right -= 1

    return True


def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    print(is_palindrome(s))
    print(is_palindrome(s2))

    print(is_palindrome_two(s))
    print(is_palindrome_two(s2))
