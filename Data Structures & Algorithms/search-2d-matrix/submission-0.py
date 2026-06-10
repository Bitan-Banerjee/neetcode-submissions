class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            # print(f"Top: {top}, Bottom: {bottom}, Mid: {mid}")

            if target > matrix[mid][0] and target > matrix[mid][-1]:
                top = mid + 1
            
            elif target < matrix[mid][0]:
                bottom = mid - 1
            
            elif target == matrix[mid][0]:
                return True

            elif target > matrix[mid][0] and target <= matrix[mid][-1]:
                l, r = 0, len(matrix[mid]) - 1
                while l <= r:
                    m = (l+r) // 2
                    if target < matrix[mid][m]:
                        r = m - 1
                    elif target > matrix[mid][m]:
                        l = m + 1
                    else:
                        return True
                return False
        return False