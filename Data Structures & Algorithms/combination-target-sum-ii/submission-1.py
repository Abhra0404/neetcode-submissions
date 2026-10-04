class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        def solve(i,sub):
            if sum(sub)==target:
                    ans.append(sub[:])
                    return
            if sum(sub)>target:
                return
            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                # if sum(sub)+nums[j]>target:
                #     break
                sub.append(nums[j])
                solve(j+1,sub)
                sub.pop()
        ans = []
        solve(0,[])
        return ans