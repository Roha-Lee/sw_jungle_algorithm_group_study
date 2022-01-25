# 226. Invert Binary Tree
# easy
# https://leetcode.com/problems/invert-binary-tree/

# 주어진 이진트리의 값을 바꿔버리는 문제.

# 파이썬다운 풀이(재귀사용)
# Runtime : 32ms (24.56%)
# Memory Usage : 14MB (1.59%)

# 연결된 노드의 자식노드를 바꾸면 어차피 해당 노드값의 위치를 바꿔도 연결관계는 사라지지 않기 떄문에 그냥 서로 교환되는 형태를 보임.
# 말단 노드부터 백트래킹으로 스왑하는 방식(Bottom-up)
# Definition for a binary tree node.
import collections
from pip import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root


# BFS 이용 풀이
# Runtime : 32ms(24.56%)
# Memory Usage : 14.2MB (53.63%)

# 부모 노드부터 스왑하면서 내려가는 방식(Top-down)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            # 부모 노드로부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left
                
                queue.append(node.left)
                queue.append(node.right)
        
        return root

# DFS 풀이
# Runtime : 64 ms(5.42%)
# Memory Usage : 14.4MB (0%)
# BFS -> popleft()로 값 추출, DFS -> pop()으로 뽑은것정도의 차이말곤 차이점 존재하지 않음.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])
        
        while queue:
            node = queue.pop()
            # 부모 노드로부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left
                
                queue.append(node.left)
                queue.append(node.right)
        
        return root