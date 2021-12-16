class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        # nums = [1,2,3,4]
        # nums = [1, 2, 2, 5, 6, 6]
        
        i = 0
        result = 0
        while i < len(nums):
            # result += min(nums[i], nums[i+1])
            result += nums[i]
            i += 2
            
        return result