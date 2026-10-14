class Solution:
    def change(self, target: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for a in range(target + 1):
                if a >= coins[i]:
                    dp[i][a] = dp[i + 1][a]
                    dp[i][a] += dp[i][a - coins[i]]

        return dp[0][target]
