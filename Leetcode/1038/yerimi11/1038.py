# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 현재 값보다 더 큰 값을 가진 모든 노드의 값의 합을 구한다 (자기 자신 값 포함)
        # 자기 자신의 값을 포함한 우측 노드의 값의 합을 구한다
        # BST의 우측 노드는 항상 부모노드보다 값이 크다는 규칙이 있기 때문
        # 중위순회 : 오른쪽-부모-왼
        
        # self.val : 지금까지 누적된 값 / root.val : 현재 노드의 값
        # 중위순회를 하면서 현재 노드의 값을 자기 자신을 포함한 지금까지의 누적된 값과 합한다
        
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)
        return root