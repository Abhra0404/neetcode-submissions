class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        def solve(start,sub):
            if sum(sub)==target:
                    ans.append(sub[:])
                    return
            if sum(sub)>target:
                return
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                if sum(sub)+nums[i]>target:
                    break
                sub.append(nums[i])
                solve(i+1,sub)
                sub.pop()
        ans = []
        solve(0,[])
        return ans