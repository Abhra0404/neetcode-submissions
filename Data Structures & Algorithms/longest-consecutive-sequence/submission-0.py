class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in seen:
            if num-1 not in seen:
                current = num
                l = 1
                while current+1 in seen:
                    l+=1
                    current+=1

                longest = max(longest,l)
        return longest