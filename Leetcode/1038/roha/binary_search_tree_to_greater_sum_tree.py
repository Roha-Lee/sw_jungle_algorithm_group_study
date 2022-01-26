# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        nums = []
        def inorder(node):
            if node is None: return 
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        inorder(root)
        nums_dict = {}
    
        temp = 0
        for i in range(len(nums)-1, -1, -1):
            nums_dict[nums[i]] = temp
            temp += nums[i]
        
        def dfs(node):
            if node is None: return 
            dfs(node.left)
            node.val += nums_dict[node.val]
            dfs(node.right)
        dfs(root)
    
        return root