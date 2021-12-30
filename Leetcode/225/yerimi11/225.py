class MyStack(object):
    
    #큐를 스택으로 구현하기
    
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        

    def pop(self):
        return self.q.popleft()
        
    def top(self):
        return self.q[0]

    def empty(self): #:rtype: bool (T/F반환)
        return len(self.q) == 0 # 0이면 true출력됨.
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()