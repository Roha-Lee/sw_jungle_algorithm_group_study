class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 조건에 맞지 않는 잘못된 풀이법 -------------------

        # 리스트에 0이 하나만 섞여있는 경우와
        # 리스트에 0이 여러개 섞여있는 경우로 볼 수 있다
        
        # 리스트에 0이 하나만 있으면 그 인덱스만 제외하고 result값을 조정
        # 리스트에 0이 여러개면 모든 결과값이 0
        
        # total = 1
        # zero_count = 0
        # zero_idx = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         total *= nums[i]
        #     else:
        #         zero_count += 1
        #         zero_idx = i
            
        # result = [0] * len(nums)
        # if zero_count >= 2:
        #     return result
        
        # elif zero_count == 1:
        #     result[zero_idx] = total
        #     return result
        
        # else:
        #     for i in range(len(nums)):
        #         result[i] = total // nums[i]

        #     return result

        nums = [1,2,3,4]

        left = [1] * len(nums)
        right = [1] * len(nums)
                
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]

        # 위 반복문이 끝나면 
        # left = [ , 1, 1*2, 1*2*3] 의 형태로 변화

        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        # 위 반복문이 끝나면 
        # right = [2*3*4, 3*4, 4, ] 의 형태로 변화
        
        # left와 right를 각 인덱스 별로 곱해주면 자기 자신을 제외한 모든 곱을 알 수 있다
        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = left[i] * right[i]
        

        return result
