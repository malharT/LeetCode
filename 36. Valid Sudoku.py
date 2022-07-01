class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        cols = []
        boxes = []
        for _ in range(9):
            rows.append([False]*9)
            cols.append([False]*9)
            boxes.append([False]*9)
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    num = int(board[row][col])-1
                    if rows[row][num]:
                        return False
                    else:
                        rows[row][num] = True
                    if cols[col][num]:
                        return False
                    else:
                        cols[col][num] = True
                    box_num = 3*(row//3) + col//3 
                    if boxes[box_num][num]:
                        return False
                    else:
                        boxes[box_num][num] = True
        return True