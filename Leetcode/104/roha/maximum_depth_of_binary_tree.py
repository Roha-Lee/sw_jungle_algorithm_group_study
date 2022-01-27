class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_node = 0
        def _max_depth(node, num_node):
            if node is None: return 
            nonlocal max_node
            if not node.left and not node.right:
                max_node = max(max_node, num_node)
                return 
            _max_depth(node.left, num_node + 1)
            _max_depth(node.right, num_node + 1)
        _max_depth(root, 1)
        return max_node