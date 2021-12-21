class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        count_arr = [0] * 20001
        
        for num in nums:
            count_arr[num + 10000] += 1
        
        sum_of_min = 0
        flag = False
        
        for i in range(20001):
            while count_arr[i]:
                if not flag:
                    sum_of_min += i - 10000
                    flag = True
                elif flag:
                    flag = False
                count_arr[i] -= 1
                
        return sum_of_min