class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(itertools.permutations(nums))
    
    
# 2----------------------------------------------------------------     

        """
        Level0: []
        level1: [1]                  [2]              [3]
        level2: [1,2]    [1,3]       [2,1] [2,3]      [3,1] [3,2]
        level3: [1,2,3]  [1,3,2]     [2,1,3][2,3,1]   [3,1,2][3,2,1]          

        """

#         def permute(self, nums: List[int]) -> List[List[int]]:
#             visited = set()
#             res = []
#             self.backtracking(res,visited,[],nums)
#             return res
#         def backtracking(self,res,visited,subset,nums):
#             if len(subset) == len(nums):
#                 res.append(subset)
#             for i in range(len(nums)):
#                 if i not in visited:
#                     visited.add(i)
#                     self.backtracking(res,visited,subset+[nums[i]],nums)
#                     visited.remove(i)
    
    
# 3----------------------------------------------------------------        
#         res = []
#         self.dfs(nums, [], res)
#         return res

#     def dfs(self, nums, path, res):
#         if not nums:
#             res.append(path)
#             # return # backtracking
#         for i in range(len(nums)):
#             self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
            
# dfs(nums = [1, 2, 3] , path = [] , result = [] )
# |____ dfs(nums = [2, 3] , path = [1] , result = [] )
# |      |___dfs(nums = [3] , path = [1, 2] , result = [] )
# |      |    |___dfs(nums = [] , path = [1, 2, 3] , result = [[1, 2, 3]] ) # added a new permutation to the result
# |      |___dfs(nums = [2] , path = [1, 3] , result = [[1, 2, 3]] )
# |           |___dfs(nums = [] , path = [1, 3, 2] , result = [[1, 2, 3], [1, 3, 2]] ) # added a new permutation to the result
# |____ dfs(nums = [1, 3] , path = [2] , result = [[1, 2, 3], [1, 3, 2]] )
# |      |___dfs(nums = [3] , path = [2, 1] , result = [[1, 2, 3], [1, 3, 2]] )
# |      |    |___dfs(nums = [] , path = [2, 1, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] ) # added a new permutation to the result
# |      |___dfs(nums = [1] , path = [2, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] )
# |           |___dfs(nums = [] , path = [2, 3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] ) # added a new permutation to the result
# |____ dfs(nums = [1, 2] , path = [3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
#        |___dfs(nums = [2] , path = [3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
#        |    |___dfs(nums = [] , path = [3, 1, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] ) # added a new permutation to the result
#        |___dfs(nums = [1] , path = [3, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] )
#             |___dfs(nums = [] , path = [3, 2, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] ) # added a new permutation to the result

    