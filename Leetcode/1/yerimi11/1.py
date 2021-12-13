nums = [3,2,4]
target = 6
# Output: [1,2]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # in을 이용한 탐색 : 모든 조합 비교X, 타겟 - 첫번째값 탐색.

    for i, n in enumerate(nums):
        complement = target - n
        
        if complement in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(complement)+(i+1)]

    # in의 시간복잡도 O(n)