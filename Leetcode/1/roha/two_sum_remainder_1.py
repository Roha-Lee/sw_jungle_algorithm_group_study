# 60ms
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)):
            remainder = target-nums[i]
            if remainder in index_dict and not i == index_dict[remainder]:
                return i, index_dict[remainder]