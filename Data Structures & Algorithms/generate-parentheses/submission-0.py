class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []

        def f(o,c):
            if o == c == n:
                ans.append("".join(stack))
                return
            if o<n:
                stack.append("(")
                f(o+1,c)
                stack.pop()
            if c<o:
                stack.append(")")
                f(o,c+1)
                stack.pop()
        f(0,0)
        return ans