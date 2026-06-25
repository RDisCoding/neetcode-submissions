class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        for row in matrix:
            row.reverse()        

        for c in range(cols):
            for r in range(rows-c-1):
                matrix[r][c], matrix[cols-1-c][rows-1-r] = matrix[cols-1-c][rows-1-r], matrix[r][c]
        
            