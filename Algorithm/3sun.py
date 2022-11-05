#  coding = utf-8 

# @Time : 2021/11/17 10:13
# @Author : HJH
# @File : 3sun.py
# @Software: PyCharm


class Solution(object):
    def three_sum(self, nums):
        number_list = sorted(nums)
        print(number_list)
        ll = len(number_list)
        target = []
        number_list.sort()

        if ll < 3:
            return target
        if ll == 3:
            if sum(number_list) == 0:
                return [number_list]
            else:
                return []

        left = 0
        right = ll - 1

        while left < right:

            if (number_list[left] + number_list[right]) * -1 in number_list[left+1: right]:
                print(left, right)
                if not [number_list[left], number_list[right], (number_list[left] + number_list[right]) * -1] in target:
                    target.append(
                        [number_list[left], number_list[right], (number_list[left] + number_list[right]) * -1])
                if number_list[left] + number_list[right] <= 0:
                    left += 1
                else:
                    right -= 1
            elif number_list[left] + number_list[right] <= 0:
                left += 1
            else:
                right -= 1

        return target


if __name__ == '__main__':

    nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
    so = Solution()
    print(so.three_sum(nums))
    print([[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]])
