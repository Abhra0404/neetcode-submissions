class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def solve(i,sub):
            if sum(sub)==target:
                    ans.append(sub[:])
                    return
            if i>=len(nums) or sum(sub)>target:
                return

            sub.append(nums[i])
            solve(i,sub)
            sub.pop()
            solve(i+1,sub)
        ans = []
        solve(0,[])
        return ans
