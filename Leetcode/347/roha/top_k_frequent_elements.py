from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntr = Counter(nums)
        result = sorted([(val, key) for key, val in cntr.items()], reverse=True)
        return [result[i][1] for i in range(k)]
            
            
        