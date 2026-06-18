class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        i, j = 0, m - 1
        while i<=j:
            row = i + (j-i)//2
            if target > matrix[row][-1]:
                i = row + 1
            elif target < matrix[row][0]:
                j = row - 1
            else: break

        x = 0
        y = n - 1
        while x<=y:
            mid = x + (y-x)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                x = mid + 1
            else:
                y = mid - 1
        return False 



