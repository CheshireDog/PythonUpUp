# coding = utf-8

"""
Author:hjh
Date:07.09
"""


class Solution:
    def toGoatLatin(self, S):
        words = S.split(' ')
        result = ''
        for index, word in zip(range(len(words)), words):
            if word[0] in 'aeiouAEIOU':
                result += ' ' + word + 'maa' + 'a'*index
            else:
                result += ' ' + word[1:] + word[0] + 'maa' + 'a'*index
        return result[1:]


if __name__ == '__main__':
    sentence = "The quick brown fox jumped over the lazy dog"
    so = Solution()
    print(so.toGoatLatin(sentence))
    print('heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa')