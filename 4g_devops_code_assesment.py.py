
""" Finds words in a given list inside of a phone number 

https://www.youtube.com/watch?v=PIeiiceWe_w

"""


def convert_words_to_numbers(words: list[str]) -> list[str]:
    """ Converts each word in the list into its numerical representation """

    letters_in_num = ['', '', 'abc', 'def', 'ghi',
                      'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    converted_words = []

    # loop through each word in array of words given
    for i in range(len(words)):
        converted_word = ''

        # loop through each letter in each word given
        for j in range(len(words[i])):

            # convert letter in word to corresponding number
            for k in range(len(letters_in_num)):
                if words[i][j] in letters_in_num[k]:
                    converted_word += str(k)

        converted_words.append(converted_word)

    return converted_words


def find_words_in_number(phone_number: str, words: list[str]) -> list[str]:
    """ Searches 'phone_number' for words found in 'words' """
    ret = []
    converted_words = convert_words_to_numbers(words)

    # check if converted word substring is found in given phone number
    for i in range(len(converted_words)):
        if converted_words[i] in phone_number:
            ret.append(words[i])

    return ret


def getValidT9Words(num: str, words: list[str]) ->list[str]:
    dic = {'2': 'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    ans = []
    for word in words:
        flag = True
        for n, c in zip(num, word):
            if c not in dic[n]:
                flag = False
                break
        if flag:
            ans.append(word)
    return ans


print(find_words_in_number('3662277', ['foo', 'bar', 'baz']))
print(find_words_in_number('2553862', ['all', 'dog', 'dumb', 'let']))

print(getValidT9Words('3662277', ['foo', 'bar', 'baz']))
print(getValidT9Words('2553862', ['all', 'dog', 'dumb', 'let']))
