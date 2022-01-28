# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        # low와 high를 포함하여 그 사이에 있는 값을 모두 더한 값을 출력한다
        # 교재 p.423
        def dfs(node):
            if not node:
                return 0
            if node.val < L:
                return dfs(node.right)
            elif node.val > R:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)
        
        return dfs(root)