class MyCircularDeque:
    
    def __init__(self, k: int):
        self.data = [None] * k
        self.max_len = k
        self.front, self.rear = 0, 0
    
    def insertFront(self, value: int) -> bool:
        if self.data[self.front] is None:
            self.data[self.front] = value
            return True
        new_loc = (self.front - 1) % self.max_len
        
        if self.data[new_loc] is None:
            self.data[new_loc] = value
            self.front = new_loc
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.data[self.rear] is None:
            self.data[self.rear] = value
            return True
        new_loc = (self.rear + 1) % self.max_len
        if self.data[new_loc] is None:
            self.data[new_loc] = value
            self.rear = new_loc
            return True
        return False
        
    def deleteFront(self) -> bool:
        if self.data[self.front] is None:
            return False
        self.data[self.front] = None
        new_loc = (self.front + 1) % self.max_len
        if self.data[new_loc] is not None:
            self.front = new_loc
        return True

    def deleteLast(self) -> bool:
        if self.data[self.rear] is None:
            return False
        self.data[self.rear] = None
        new_loc = (self.rear - 1) % self.max_len
        if self.data[new_loc] is not None:
            self.rear = new_loc
        return True

    def getFront(self) -> int:
        if self.data[self.front] is None:
            return -1 
        return self.data[self.front]
        

    def getRear(self) -> int:
        if self.data[self.rear] is None:
            return -1 
        return self.data[self.rear]
        

    def isEmpty(self) -> bool:
        return self.data[self.front] is None
        

    def isFull(self) -> bool:
        return self.front == (self.rear + 1) % self.max_len and self.data[self.front]
        


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