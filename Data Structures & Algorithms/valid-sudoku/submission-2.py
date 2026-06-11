class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                val = board[i][j]

                if val in rows[i] or val in cols[j] or val in boxes[(i//3,j//3)]:
                    return False
                
                rows[i].add(val)
                cols[j].add(val)
                boxes[i//3, j//3].add(val)

        return True
                


                    
        