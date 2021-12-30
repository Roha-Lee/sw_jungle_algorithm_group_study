
class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [None] * k
        self.max_num = k
        self.front = 0
        self.rear = -1
        

    def enQueue(self, value: int) -> bool:
        next_pos = (self.rear + 1) % self.max_num
        if self.data[next_pos] is None: 
            self.data[next_pos] = value
            self.rear = next_pos
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        if self.data[self.front] is None: return False
        self.data[self.front] = None
        self.front = (self.front + 1) % self.max_num
        return True

    def Front(self) -> int:
        if self.data[self.front] is None: return -1
        return self.data[self.front]
        

    def Rear(self) -> int:
        if self.data[self.rear] is None: return -1
        return self.data[self.rear]
    

    def isEmpty(self) -> bool:
        return self.data[self.front] is None
        
    def isFull(self) -> bool:
        if self.data[self.rear] is None:
            return False
        return (self.rear - self.front) % self.max_num == self.max_num - 1
        
            
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()