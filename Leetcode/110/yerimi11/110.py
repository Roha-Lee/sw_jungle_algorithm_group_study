# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 리프노드부터 자식노드까지 depth를 count 했을 때, 왼쪽/오른쪽의 차이가 1보다 크면 false 출력
        # 재귀로 높이 차이 계산
        
        def DFS(root):
            if not root:
                return 0 # Null node
            
            left = DFS(root.left) # 맨 아래 노드까지 내려감
            right = DFS(root.right)
            
            # 높이 차이가 1보다 더 나는 경우 계속해서 -1만 나옴, 이외에는 윗 노드로 올라갈 때마다 +1
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return max(left, right) + 1
        
        # -1이 아닐 때 정상적인 균형 이진트리로 판명, true 리턴
        return DFS(root) != -1 
        
        
        
        # -------------------------
        
#         if root == None:
#             return true
#         l = self.depth(root.left)
#         r = self.depth(root.right)
#         return (abs(l-r) < 2) and self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
#         def depth(self, node):
#             if node == None:
#                 return 0 # 맨 아래 리프노드 0
#             return max(self.depth(node.left), self.depth(node.right)) + 1 # 위로 올라갈 때 마다 1씩 증가
        
        
        
        
        # ----- Counting depth -----
         
        # self.result = 0
        
        # 트리문제 -> 재귀
#         def DFS1(root, count = 1, maxc_l = 0, maxc_r = 0): # 전위 preorder
#             if root == None :     # 자식노드가 없으면 종료
#                 count -= 1
#                 maxc_l = max(self.result, count)
#                 # self.result = maxc_l
                
#                 # 굳이 차 케이스를 두개로 안나누고 abs()를 쓰자.!! (아직 구현 안함)
#                 if maxc_l > maxc_r:
#                     if (maxc_l - maxc_r) > 1:
#                         return false # 여기서 에러 남
#                 elif (maxc_r - maxc-l) <= 1:
#                     return true
#                 # return
#             else:
#                 DFS1(root.left, count+1)  # 왼쪽 자식 노드 탐색
#                 DFS2(root.right, count+1)
                
                
#         def DFS2(root, count = 1, maxc_l = 0, maxc_r = 0): # 전위 preorder
#             if root == None :     # 자식노드가 없으면 종료
#                 count -= 1
#                 maxc_r = max(self.result, count)
#                 # self.result = maxc_r
#                 if maxc_l > maxc_r:
#                     if (maxc_l - maxc_r) > 1:
#                         return false
#                 elif (maxc_r - maxc-l) <= 1:
#                     return true
#                 # return
#             else:
#                 DFS1(root.left, count+1, maxc_l, maxc_r)  # 왼쪽 자식 노드 탐색
#                 DFS2(root.right, count+1, maxc_l, maxc_r)
                 

#         DFS1(root)
#         DFS2(root)
    
        # -----    -----   -----   -----
