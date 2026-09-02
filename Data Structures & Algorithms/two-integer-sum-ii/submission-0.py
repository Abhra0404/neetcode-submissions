class Solution:
    def twoSum(self, arr: List[int], x: int) -> List[int]:
        i=0
        j=len(arr)-1
        while i<j:
            if arr[i]+arr[j]==x:
                return [i+1,j+1]
            elif arr[i]+arr[j]>x:
                j-=1
            else:
                i+=1
        