class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def get_diameter(node):
            nonlocal result
            if node is None: return 0
            left, right = get_diameter(node.left), get_diameter(node.right)
            result = max(result, left + right)
            return max(left, right) + 1
        get_diameter(root)
        return result