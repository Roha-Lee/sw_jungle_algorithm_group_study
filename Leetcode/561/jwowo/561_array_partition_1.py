class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:        
        nums.sort()
        ans = 0

        for idx, val in enumerate(nums):
            if not idx % 2:
                ans += val
                
        return ans