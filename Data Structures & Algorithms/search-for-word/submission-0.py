class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])

        def bt(r,c,k):
            if k == len(word): return True

            if r<0 or c<0 or r>=row or c>=col or board[r][c] != word[k]:
                return False
            
            temp = board[r][c]
            board[r][c] = "#"
            res = (bt(r-1, c, k+1) or bt(r+1,c,k+1) or bt(r,c-1,k+1) or bt(r,c+1,k+1))

            board[r][c] = temp
            return res
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if bt(r,c,0):
                        return True
        return False
