#  coding = utf-8 

# @Time : 2021/3/4 19:28
# @Author : HJH
# @File : SortMethod.py
# @Software: PyCharm


class Sort():
    def bubble_sort(self, arr):
        n = len(arr)
        if n < 2:
            return arr
        for j in range(n):
            for i in range(n-j-1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return arr


if __name__ == '__main__':
    arr = [6, 5, 4, 3, 2, 1]
    so = Sort()
    print(so.bubble_sort(arr))
