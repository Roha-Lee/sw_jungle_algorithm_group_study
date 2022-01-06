# 1차원 리스트로 구현
class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = [None] * k     # queue 역할을 하는 1차원 리스트
        self.maxlen = k         # 입력 받을 최대 길이
        self.front = 0          # 맨 앞 원소의 인덱스
        self.rear = 0           # 맨 뒤 원소의 다음 인덱스


    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.q[self.front-1] is None:
            self.q[self.front-1] = value # 0 인덱스에 1이 삽입 
            self.front = (self.front - 1) % self.maxlen # front를 한 칸 앞으로 옮긴다
            return True
        else:
            return False


    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.q[self.rear] is None:       # 삽입된 맨 끝 원소의 다음 위치 = rear
            self.q[self.rear] = value       # 0 인덱스에 1이 삽입
            self.rear = (self.rear + 1) % self.maxlen   # 일자형 큐라면 단지 rear에 +1을 하겠지만 원형 큐이므로 %연산자로 max길이를 초과할 경우 0인덱스로 돌아가게 만듦.
            return True
        else:
            return False


    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.q[self.front] is None:      # 뺄 원소가 없다 = 큐가 비었다
            return False
        else:
            self.q[self.front] = None       # front 위치에 None 값 넣기
            self.front = (self.front + 1) % self.maxlen   # front도 마찬가지로 maxlen보다 커지면 인덱스가 0으로 향하게끔 나머지 연산
            return True


    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.q[self.rear - 1] is None:  
            return False
        else:
            self.q[self.rear - 1] = None	# rear는 맨 뒷 원소의 다음 위치니까 -1
            self.rear = (self.rear - 1) % self.maxlen	# rear는 값이 있는 위치의 뒤에 있어야 하니 삭제된 자리의 앞으로 이동
            return True

    def getFront(self):
        """
        :rtype: int
        """
        return -1 if self.q[self.front] is None else self.q[self.front]


    def getRear(self):
        """
        :rtype: int
        """
        # rear의 인덱스가 0인 경우에도 커버. 인덱스가 -1이 되는데, 파이썬에서는 리스트 인덱스에 [-1]넣으면 맨 뒷 원소 나오잖아.
        return -1 if self.q[self.rear - 1] is None else self.q[self.rear - 1]   


    def isEmpty(self):
        """
        :rtype: bool
        """
        # 프론트와 리어가 같고 그 둘중 하나의 위치의 값이 None이면 큐에 아무것도 없다는 뜻
        return self.front == self.rear and self.q[self.front] is None


    def isFull(self):
        """
        :rtype: bool
        """
        # 프론트와 리어가 같고 그 둘중 하나의 위치의 값이 None이 아니라 다른 값이 있다면 큐가 다 찼다는 뜻
        return self.front == self.rear and self.q[self.front] is not None



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


# 이중 링크드 리스트로 구현
# class ListNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class MyCircularDeque(object):

#     def __init__(self, k):
#         """
#         :type k: int
#         """
#         self.head, self.tail = ListNode(None), ListNode(None)
#         self.k, self.len = k, 0
#         self.head.right, self.tail.left = self.tail, self.head

        
#     def _add(self, node, new):
#         n = node.right
#         node.right = new
#         new.left, new.right = node, n
#         n.left = new
    
    
#     def _del(self, node):
#         n = node.right.right
#         node.right = n
#         n.left = node
        
        
#     def insertFront(self, value):
#         """
#         :type value: int
#         :rtype: bool
#         """
#         if self.len == self.k:
#             return False
#         self.len += 1
#         self._add(self.head, ListNode(value))
#         return True
        

#     def insertLast(self, value):
#         """
#         :type value: int
#         :rtype: bool
#         """
#         if self.len == self.k:
#             return False
#         self.len += 1
#         self._add(self.tail.left, ListNode(value))
#         return True
        

#     def deleteFront(self):
#         """
#         :rtype: bool
#         """
#         if self.len == 0:
#             return False
#         self.len -= 1
#         self._del(self.head)
#         return True
        

#     def deleteLast(self):
#         """
#         :rtype: bool
#         """
#         if self.len == 0:
#             return False
#         self.len -= 1
#         self._del(self.tail.left.left)
#         return True
        

#     def getFront(self):
#         """
#         :rtype: int
#         """
#         return self.head.right.val if self.len else -1
        

#     def getRear(self):
#         """
#         :rtype: int
#         """
#         return self.tail.left.val if self.len else -1
        

#     def isEmpty(self):
#         """
#         :rtype: bool
#         """
#         return self.len == 0
        

#     def isFull(self):
#         """
#         :rtype: bool
#         """
#         return self.len == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()