# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.result = 0
        
        # 트리문제 -> 재귀
        def DFS(root, count = 1): # 전위 preorder
            if root == None :     # 자식노드가 없으면 종료
                count -= 1
                maxc = max(self.result, count)
                self.result = maxc
                return
            else:
                DFS(root.left, count+1)  # 왼쪽 자식 노드 탐색
                DFS(root.right, count+1) # 오른쪽 자식 노드 탐색
                 

        DFS(root)
        return self.result
        