
from collections import defaultdict

# https://leetcode.com/problems/valid-sudoku/S


def is_valid_sudoku(board):
    # Time O(9^2)
    # Space: O(9^2)
    cols = defaultdict(set)  # key = col num, val = set of values
    rows = defaultdict(set)
    squares = defaultdict(set)  # key = (r / 3, c /3)

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                return False

            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

    print(squares)
    return True


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                          ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    board2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".",
                                                                                                                                                                                                           "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print(is_valid_sudoku(board))
    print(is_valid_sudoku(board2))
