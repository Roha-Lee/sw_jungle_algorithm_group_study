class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:        
        return sum(v for i, v in enumerate(sorted(nums)) if not i%2)