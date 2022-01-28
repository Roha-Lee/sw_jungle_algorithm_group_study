class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = [None] * k     # queue 역할을 하는 1차원 리스트
        self.maxlen = k         # 입력 받을 최대 길이
        self.front = 0          # 맨 앞 원소의 인덱스
        self.rear = 0           # 맨 뒤 원소의 인덱스

    def enQueue(self, value):
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
        

    # dequeue : front 포인터 이동
    def deQueue(self):
        """
        :rtype: bool
        """
        if self.q[self.front] is None:      # 뺄 원소가 없다 = 큐가 비었다
            return False
        else:
            self.q[self.front] = None       # front 위치에 None 값 넣기
            self.front = (self.front + 1) % self.maxlen     # front도 마찬가지로 maxlen보다 커지면 인덱스가 0으로 향하게끔 나머지 연산
            return True
            
        
        

    def Front(self):
        """
        :rtype: int
        """
        return -1 if self.q[self.front] is None else self.q[self.front]
        

    def Rear(self):
        """
        :rtype: int
        """
        # rear의 인덱스가 0인 경우에도 커버. 인덱스가 -1이 되는데, 파이썬에서는 리스트 인덱스에 [-1]넣으면 맨 뒷 원소 나오잖아.
        return -1 if self.q[self.rear - 1] is None else self.q[self.rear - 1]   
    
#       실패작
#         if not self.q:
#             rear_idx = 0        # 임시로 끝 원소의 인덱스를 가리키는 변수
#             if self.rear == 0:  # rear가 0인 경우 = 큐가 다 찼다. -> 맨 끝값을 가리키게 하려면 rear_idx가 큐의 맨 뒤의 인덱스를 가리키게만 하면 된다.
#                 rear_idx = maxlen - 1
#             else:               # 0이 아닌 경우는 -1만 해주면 된다.
#                 rear_idx = self.rear - 1
                
#             return self.q[rear_idx]
#         else:
#             return -1
         

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
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()