class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans,curr = [],[]

        def f(i):
            if i == n:
                ans.append(curr[:])
                return
            f(i+1)
            curr.append(nums[i])
            f(i+1)
            curr.pop()
        f(0)
        return ans