class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def _merge(node1, node2):
            if node1 and node2:
                new_node = TreeNode(node1.val + node2.val)            
            elif node1:
                new_node = TreeNode(node1.val)
            elif node2:
                new_node = TreeNode(node2.val)
            else: 
                return None
            new_node.left = _merge(node1.left if node1 and node1.left else None, node2.left if node2 and node2.left else None)
            new_node.right = _merge(node1.right if node1 and node1.right else None, node2.right if node2 and node2.right else None)
            return new_node
        return _merge(root1, root2)