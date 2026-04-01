class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows*cols - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // cols
            col = mid % cols
            num = matrix[row][col]
            if num == target:
                return True
            elif num > target:
                right = mid - 1
            else:
                left = mid + 1

        return False