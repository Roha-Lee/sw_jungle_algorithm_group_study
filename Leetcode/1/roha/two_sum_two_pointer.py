# Two pointers 64ms
from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = defaultdict(list)
        for idx, num in enumerate(nums):
            index_dict[num].append(idx)
        nums = sorted(nums)
        start, end = 0, len(nums)-1
        
        while start < end:
            temp_sum = nums[start] + nums[end]
            if temp_sum > target:
                end -= 1
            elif temp_sum < target:
                start += 1
            else:
                if nums[start] == nums[end]:
                    return index_dict[nums[start]]
                else:
                    return index_dict[nums[start]][0], index_dict[nums[end]][0]