class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.
        # 정렬하고, 투포인터로 다 돌면서 합해보기?
        results = []
        nums.sort() # nums = [-4, -1, -1, 0, 1, 2]
        # 앞에 두 개 먼저 더하고 그 다음 인덱스부터 투포인터 돌려서 더해보기
        
        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # 간격을 좁혀가며 합 sum 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # sum = 0인 경우이므로 정답 및 스킵 처리
                    results.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return results    
                
        