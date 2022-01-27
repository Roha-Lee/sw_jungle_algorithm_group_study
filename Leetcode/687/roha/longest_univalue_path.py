class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        result = 0
        def get_longest_univalue_path(node, parent_val = 0):
            nonlocal result
            if node is None: return 0
            left = get_longest_univalue_path(node.left, node.val)
            right = get_longest_univalue_path(node.right, node.val)
            result = max(result, left + right)
            if parent_val == node.val:
                return max(left, right) + 1
            return 0
        get_longest_univalue_path(root)
        return result