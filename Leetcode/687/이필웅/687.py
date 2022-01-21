# LeetCode 687. Longest Univalue Path
# Medium
# https://leetcode.com/problems/longest-univalue-path/

# 같은 값을 갖는 연속된 노드의 길이를 리턴하는 문제.
# Runtime : 408ms(33.54%)
# Memory Usage : 18.1MB (53.4%)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    result : int = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            
            self.result = max(self.result, left + right)
            
            return max(left,right)
        dfs(root)
        return self.result