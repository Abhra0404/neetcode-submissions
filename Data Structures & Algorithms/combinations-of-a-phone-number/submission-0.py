class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def f(i,curr):
            if len(curr)==len(digits):
                ans.append(curr)
                return
            for c in digitToChar[digits[i]]:
                f(i+1,curr+c)
        if digits:
            f(0,"")
        return ans