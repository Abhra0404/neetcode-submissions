class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1]*n
        def f(i):
            if i==n:
                return 1
            if dp[i]!=-1: return dp[i]
            one,two = 0,0
            if s[i]!='0':
                one = f(i+1)
            if i+1<n and s[i]!='0' and int(s[i:i+2])<=26:
                two = f(i+2)
            dp[i] = one+two
            return dp[i]
        return f(0)