class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [] 
        self.temp = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.temp:
            while self.data:
                self.temp.append(self.data.pop())
        return self.temp.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.temp:
            while self.data:
                self.temp.append(self.data.pop())
        return self.temp[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.data) + len(self.temp) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()