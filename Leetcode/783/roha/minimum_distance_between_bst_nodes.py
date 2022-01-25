class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        result = []
        def inorder(node):
            if node is None: return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)
        return min([abs(result[i] - result[i+1]) for i in range(len(result) - 1)])