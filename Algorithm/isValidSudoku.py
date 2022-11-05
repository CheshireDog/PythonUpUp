#  coding = utf-8 

# @Time : 2021/7/26 20:04
# @Author : HJH
# @File : isValidSudoku.py
# @Software: PyCharm


class Solution:
    def isValidSudoku(self, board) -> bool:
        check = []
        # for i in board:
        #     for j in i:
        #         if not j == '.':
        #             check.append(j)
        #     if not len(check) == len(set(check)):
        #         return False
        #     else:
        #         check = []
        for i in range(9):
            for j in range(9):
                if not board[j][i] == '.':
                    check.append(board[j][i])
            if not len(check) == len(set(check)):
                return False
            else:
                check = []
        for i in range(9):
            for j in range(9):
                if not board[i][j] == '.':
                    check.append(board[i][j])
            if not len(check) == len(set(check)):
                return False
            else:
                check = []
        starts = [[0, 0], [3, 0], [6, 0], [0, 3], [3, 3], [6, 3], [0, 6], [3, 6], [6, 6]]
        for start in starts:
            for i in range(3):
                for j in range(3):
                    x = start[0] + i
                    y = start[1] + j
                    if not board[x][y] == '.':
                        check.append(board[x][y])
            if not len(check) == len(set(check)):
                return False
            else:
                check = []
        return True


if __name__ == '__main__':
    so = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(so.isValidSudoku(board))
