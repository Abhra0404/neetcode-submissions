class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r =  len(matrix)
        c =  len(matrix[0])
        total = r*c
        lo = 0 
        hi = total -1

        while lo<=hi:
            mid = lo + (hi - lo) // 2
            rp = mid//c
            cp = mid%c
            if matrix[rp][cp] < target:
                lo = mid + 1
            elif matrix[rp][cp] > target:
                hi = mid -1
            else:
                return True
        
        return False