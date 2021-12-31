class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)
        
            
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        for _ in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
            
        result = self.stack2.pop()
        
        for _ in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        
        return result

    def peek(self) -> int:
        """
        Get the front element.
        """
        for _ in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        
        result = self.stack2[-1]
        
        for _ in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        
        return result
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True
        else:
            return False