class MyQueue(object):

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
        self.peek()
        return self.output.pop()
        

    def peek(self): # 큐 처음에 있는 요소를 조회한다
        """
        :rtype: int
        """
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.ouput[-1]
        

    def empty(self): # bool타입 리턴
        return self.input == [] and self.output == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()