from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        nums = sorted(nums)
        idx_dict = defaultdict(list)
        for i, num in enumerate(nums):
            idx_dict[num].append(i)
        
        for s_ptr in range(len(nums)-1):
            if s_ptr > 0 and nums[s_ptr] == nums[s_ptr-1]:
                    continue    
            for e_ptr in range(len(nums)-1, s_ptr, -1):
                if e_ptr < len(nums)-1 and nums[e_ptr] == nums[e_ptr + 1]:
                    continue
                remainder = -(nums[s_ptr] + nums[e_ptr])   
                if not idx_dict[remainder]:
                    continue
                for idx in idx_dict[remainder]:
                    if s_ptr < idx < e_ptr:
                        results.add((nums[s_ptr], nums[e_ptr], remainder))
                        break
        return list(results)            
    