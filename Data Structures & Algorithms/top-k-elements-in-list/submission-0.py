class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        sort = sorted(freq, key=freq.get, reverse=True)
        top_k = sort[:k]
        return top_k