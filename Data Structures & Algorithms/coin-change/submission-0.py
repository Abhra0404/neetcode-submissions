class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def f(x):
            if x==0: return 0
            if x in memo:
                return memo[x]
            res = 1e9
            for coin in coins:
                if x-coin>=0:
                    res = min(res, 1+f(x-coin))
            memo[x] = res
            return res
        ans = f(amount)
        return -1 if ans>=1e9 else ans