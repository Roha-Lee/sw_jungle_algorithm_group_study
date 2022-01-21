# LeetCode 543. Diameter of Binary Tree
# Easy
# https://leetcode.com/problems/diameter-of-binary-tree/

# 주어진 이진 탐색 트리의 직경을 탐사하는 문제
# 이진트리에서 두 노드 간 가장 긴 경로의 길이를 출력하는 문제.

# Runtime : 59ms(62.35%)
# Memory Usage : 16.5MB (72.96%)

# Definition for a binary tree node.
from pip import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    longest : int = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return -1
            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 가장 긴 경로
            self.longest = max(self.longest, left+ right +2)
            # 상태값
            return max(left, right) + 1
    
        dfs(root)
        return self.longest