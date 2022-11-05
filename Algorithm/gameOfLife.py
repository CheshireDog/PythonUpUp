#  coding = utf-8 

# @Time : 2022/9/11 22:20
# @Author : HJH
# @File : gameOfLife.py
# @Software: PyCharm


class Solution:
    def gameOfLife(self, board) -> None:
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                count = board[i-1][j-1]+board[i-1][j]+board[i-1][j+1]+board[i][j-1]+board[i][j+1]+board[i+1][j-1]+\
                        board[i+1][j]+board[i+1][j+1]
                if


