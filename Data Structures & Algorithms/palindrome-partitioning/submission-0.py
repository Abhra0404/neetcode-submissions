class Solution:
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        ans,curr =[],[]
        def f(i):
            if i>=len(s):
                ans.append(curr[:])
                return
            for j in range(i,len(s)):
                if self.isPali(s,i,j):
                    curr.append(s[i:j+1])
                    f(j+1)
                    curr.pop()
        f(0)
        return ans