# coding = utf-8

"""
Author:hjh
Date:07.09
"""

class Solution:
    def isPalindrome(self, s):
        import re
        target = re.sub('[^\u4e00-\u9fa5^a-z^A-Z^0-9]', '', s)
        if target[::-1].lower() == target.lower():
            return True
        else:
            return False

    def isPalindrome2(self, s):
        import re
        target = re.sub('[^a-z^A-Z^0-9]', '', s)
        return target[::-1].lower() == target.lower()


if __name__ == '__main__':
    string = "A man, a plan, a canal: Panama"
    so = Solution()
    print(so.isPalindrome(string))
