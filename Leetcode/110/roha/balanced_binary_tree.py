class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def _is_balanced(node):
            if node is None: return True, 0
            left_flg, left_height = _is_balanced(node.left)
            right_flg, right_height = _is_balanced(node.right)
            if not left_flg or not right_flg:
                return False, max(left_height, right_height) + 1
            if abs(left_height - right_height) > 1:
                return False, max(left_height, right_height) + 1
            return True, max(left_height, right_height) + 1
        result, _ = _is_balanced(root)
        return result 