#  coding = utf-8 

# @Time : 2022/8/30 14:41
# @Author : HJH
# @File : removeDuplicateLetters.py
# @Software: PyCharm

import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        result = ''
        counter = {}
        for l in s:
            if l in counter:
                counter[l] += 1
            else:
                counter[l] = 1
        for letter in s:
            print('处理字符'+letter)
            if letter not in result:
                result += letter
                print(result)
            else:
                index = result.find(letter)
                for i in result[index + 1:]:
                    print('当前比对:' + i)
                    if i < letter:
                        result = result.replace(letter, '')
                        print('删除字符' + result)
                        result += letter
                        print('末尾添加' + result)
                        break
        return result

    def removeDuplicateLetters2(self, s) -> int:
        stack = []
        remain_counter = collections.Counter(s)

        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and remain_counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            remain_counter[c] -= 1
        return ''.join(stack)


if __name__ == '__main__':
    so = Solution()
    ss = 'cbacdcb'
    print(so.removeDuplicateLetters2(ss))
