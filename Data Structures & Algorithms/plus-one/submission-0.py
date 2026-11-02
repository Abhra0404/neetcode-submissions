class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits)))  # '123' → 123
        num+=1
        result = []
        for i in str(num):
            result.append(int(i))
        return result