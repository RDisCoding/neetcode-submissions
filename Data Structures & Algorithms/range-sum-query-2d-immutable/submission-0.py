class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.nummatrix = [[0]*(cols+1) for x in range(rows+1)]
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                self.nummatrix[i][j] = matrix[i-1][j-1] + self.nummatrix[i-1][j] + self.nummatrix[i][j-1] - self.nummatrix[i-1][j-1]
        
        print(self.nummatrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        angle = self.nummatrix[row2+1][col2+1] - self.nummatrix[row1][col2+1] - self.nummatrix[row2+1][col1] + self.nummatrix[row1][col1]
        return angle