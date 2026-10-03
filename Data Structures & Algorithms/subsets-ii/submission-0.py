class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def f(i,sub):        
            ans.append(sub[:])
            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                sub.append(nums[j])
                f(j+1,sub)
                sub.pop()
        f(0,[])
        return ans



