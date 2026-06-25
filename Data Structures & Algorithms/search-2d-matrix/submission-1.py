class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix)-1
        row = 0
        while i<=j:
            mid = i + (j-i)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                row = mid
                break
            elif target< matrix[mid][0]:
                j = mid - 1
            else:
                i = mid + 1
        
        i = 0; j = len(matrix[0])-1
        while i<=j:
            mid = i + (j-i)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid]< target:
                i = mid +1
            else:
                j = mid - 1
        return False