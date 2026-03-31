class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_num = len(matrix)
        target_row = 0
        for r in range(row_num):
            print(matrix[r][-1])
            if target <= matrix[r][-1]:
                target_row = r
                break
        target_list = matrix[target_row]
        print(target_row)
        l, r = 0, len(target_list) - 1
        print(target_list)
        while l <= r:
            mid = (l + r) // 2
            if target_list[mid] > target:
                r = mid - 1
            elif target_list[mid] < target:
                l = mid + 1
            else:
                return True

        return False

            
        