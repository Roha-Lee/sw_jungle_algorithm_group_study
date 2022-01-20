# LeetCode 617. Merge Two Binary Trees
# https://leetcode.com/problems/merge-two-binary-trees/

# 주어진 두개의 이진트리를 하나의 트리로 합치는 문제

# 별도의 node를 따로 만들어서 푼 방식
# Runtime : 146ms(85.35%)
# Memory Usage : 15.3MB(6.86%)

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            
            return node
        else:
            return root1 or root2
        

# 별도의 노드를 만들지 않고 기존의 이진트리 하나에 합쳐서 푼 풀이방법
# Runtime : 84ms(15.3%)
# Memory Usage : 15.5MB(70.74%)

class Solution2:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return
        elif not root1:
            return root2
        elif not root2:
            return root1
        
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1