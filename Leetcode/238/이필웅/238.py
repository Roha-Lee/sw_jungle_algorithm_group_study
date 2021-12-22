# LeetCode 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/submissions/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        
        return output

nums = [1,2,3,4]
list = []
def multi(x):
    if len(x) == 0:
        return 'not list'
    if len(x) == 1:
        return x[0]
    ans = 1
    for i in x:
        ans *= i
    
    return ans 

for i in range(len(nums)):
    a = nums[:i]
    b = nums[i+1:]
    if len(a) == 0:
        list.append(multi(b))
    if len(b) == 0:
        list.append(multi(a))
    if len(a) != 0 and len(b) != 0:
        list.append(multi(a)*multi(b))

print(list)
