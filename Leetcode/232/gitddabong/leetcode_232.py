class MyQueue(object):
    
    # 스택으로 큐 구현하기
    # 사용할 수 있는 연산 : 
    # append, pop()
    

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.input.append(x)
        
    def pop(self):
        """
        :rtype: int
        """
        # 왼쪽에서 요소 제거를 어떻게 구현하나?
        self.peek()
        return self.output.pop()
    
    def peek(self):
        """
        :rtype: int
        """
        # output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
        
    def empty(self):
        """
        :rtype: bool
        """
        return len(self.input) == 0 and len(self.output) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()