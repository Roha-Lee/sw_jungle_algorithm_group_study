class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        def inorder(node):
            nonlocal result
            if node is None: return
            inorder(node.left)
            if low <= node.val <= high:
                result += node.val
            inorder(node.right)
        inorder(root)
        return result