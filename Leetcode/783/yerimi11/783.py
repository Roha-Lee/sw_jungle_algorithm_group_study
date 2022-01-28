# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Binary Search Tree (BST)
        # 두 노드가 가진 값의 차이 최솟 값 출력
        
        # 연결리스트니까 주어진 값 중에 최솟값 2개 뽑아서 차이 구하는 방법은 안된다
        # 노드 탐색하면서 val값이 min인 것 따로 저장해둔다 (min1, min2 이렇게 2개)
        # 아니지 val가 작은게 문제가 아니라, 49-48이어도 차이가 1인 것을 찾을 줄도 알아야하네.
        # null은 pass
        
        # DFS로 비교. 4고정 4-2, 4-1, 4-3 => 4-6 (음수는 pass)
        # 대박,, BST의 특징 -> 자기 자식의 왼쪽노드는 무조건 자기보다 작음 ;; 깜빡했음 ㅋㅋ
        # 그럼 생각 해보쟈구
        # (현재 루트 노드 - 왼쪽 자식 노드) 의 val을 구해서 temp에 저장해두고
        # 오른쪽으로 갈 때는 (오른쪽 자식 노드 - 현재 루트 노드) 구해서 res = min(temp, 계산값) 해서 출력하면 될 듯
#         self.res = float('inf')
        
#         def DFS(root):
#             if root is None:
#                 return
            
# #             if root is 'null':
# #                 pass
        
#             if root.left:
#                 temp = root.val - root.left.val
#                 self.res = min(self.res, temp)
                
#             if root.right:
#                 temp = root.right.val - root.val
#                 self.res = min(self.res, temp)
                
#             DFS(root.left)
#             DFS(root.right)

        
#         DFS(root)
#         return self.res            
            
#         # 지금 '모든' 노드와 비교가 다 안되는 듯?
#         # 왼쪽 서브트리의 가장 오른쪽 노드와
#         # 오른쪽 서브트리의 가장 왼쪽 노드를 찾아야 함
        
                # 이진 탐색 트리에서 루트와 가장 근사한 값을 가지는 노드는 총 2개.
        # 왼쪽 서브트리에서 가장 오른쪽의 노드, 오른쪽 서브트리에서 가장 왼쪽의 노드다.
        # 모든 노드를 순회하며 각 노드와 이 둘만 비교해서 차이값의 최솟값을 저장
        
        
        self.result = float('inf')
        
        def search_left(root):
            curr = root.left
            while curr.right:
                curr = curr.right
            
            return curr.val
        
        
        def search_right(root):
            curr = root.right
            while curr.left:
                curr = curr.left
                
            return curr.val
            

        def dfs(root):
            if root is None:
                return
            
            max_left = 1000000     # 딱히 의미 없는 엄청 큰 값
            min_right = 1000000
            if root.left:
                max_left = search_left(root)
            
            if root.right:
                min_right = search_right(root)
            
            self.result = min(self.result, abs(root.val - max_left), abs(min_right - root.val))
            
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return self.result
    
    # 시간복잡도 : while문 각각 o(log(n))
    # 모든 노드에 대해서 저 연산들을 반복해야되니까 o(n(log(n)))
    
        
        