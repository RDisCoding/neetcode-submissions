class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        l, r = 0, row - 1
        while l<=r:
            mid = (l+r)//2
            if matrix[mid][0] <= target <= matrix[mid][col - 1]:
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
            
        targetRow = mid
        l=0
        r= col - 1
        while l<=r:
            mid = (l+r)//2
            if target == matrix[targetRow][mid]:
                return True
            elif target < matrix[targetRow][mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False
