# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        # 두 트리를 하나로 합치기
        # 두 노드 자리가 겹치는 경우 해당 자리의 노드는 두 값을 더함
        # ex) root1 : 1, root2 : 2 => merge root node : 1+2 = 3

        # 리스트 값 순서대로 sum 하면 되려나? 연결리스트니까 val를 더해야할거고..
        # -----
        
        # max_len = max(len(root1), len(root2)) # 연결리스트라서 길이 셀 수 없음 -> while문으로 바꾸자
        # result = ''
        
        if root1 is None and root2 is None:
            return None
        
        elif root1 is None:
            result = root2
        elif root2 is None:
            result = root1
        
        else:    
            result = TreeNode(root1.val + root2.val)
            result.left = self.mergeTrees(root1.left, root2.left)
            result.right = self.mergeTrees(root1.right, root2.right)
            
        # while root1 or root2:
                
            # sum_val = root1.val + root2.val
            # result.append(sum_val) # 아 이걸 트리(연결리스트)로 만들어줘야 할 듯
            # root1.pop()
            # root2.pop()

            
        return result