class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def dfs(r,c,l):
            if l == len(word): 
                return True
                
            if r<0 or c<0 or r>=row or c>=col or board[r][c] == "#" or board[r][c] != word[l]:
                return False
            
            temp = board[r][c]
            board[r][c] = "#"
            print(r)
            print(c)
            print(l)
            print()
            ans = dfs(r+1,c,l+1) or dfs(r-1,c,l+1) or dfs(r,c-1,l+1) or dfs(r,c+1,l+1)

            board[r][c] = temp
            return ans

        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        
        return False