class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr = []
        ans = []
        n = len(nums)
        visited = [False]*n
        def f(i):
            if i == n:
                ans.append(curr[:])
                return
            for num in range(n):
                if visited[num]:
                    continue
                curr.append(nums[num])
                visited[num] = True
                f(i+1)
                curr.pop()
                visited[num] = False
        f(0)
        return ans
