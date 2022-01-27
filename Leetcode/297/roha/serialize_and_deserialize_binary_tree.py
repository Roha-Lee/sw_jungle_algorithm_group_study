from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        if root is None: return ','.join(result)
        q = deque([root])
        
        
        while q:
            curr = q.popleft()
            if curr is None:
                result.append('None')
                continue
            else:
                result.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
        return ','.join(result).strip(',None')
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if data == '': return None
        data = data.split(',')
        root = TreeNode(int(data[0]))
        q = deque([root])
        idx = 1
        while q:
            curr = q.popleft()
            if curr is None:
                continue
            
            if idx < len(data):
                if data[idx] == 'None':
                    curr.left = None
                else:
                    curr.left = TreeNode(int(data[idx]))
                    q.append(curr.left)
                idx += 1
            if idx < len(data):
                if data[idx] == 'None':
                    curr.right = None
                else:
                    curr.right = TreeNode(int(data[idx]))
                    q.append(curr.right)
                idx += 1
        return root