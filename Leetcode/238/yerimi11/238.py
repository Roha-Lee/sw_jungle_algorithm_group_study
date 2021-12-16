# 정수 배열 nums가 주어지면 answer[i]가 nums[i]를 제외한 nums의 모든 요소의 곱과 같도록 배열 응답을 반환합니다.
# 숫자의 접두사 또는 접미사의 곱은 32비트 정수에 맞도록 보장됩니다.
# 나누기 연산을 사용하지 않고 O(n) 시간에 실행되는 알고리즘을 작성해야 합니다.
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ## 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라. 주의 : 나눗셈 하지 않고 O(n)에 풀이하라
#         multi = []
        
#         for i in range(len(nums)):
#             # if i:
#                 # continue    
#             multi = multi * nums[i]
        
        # 풀이가 다 똑같네
        out = []
        p =1
        # 왼쪽 곱셈
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out
        