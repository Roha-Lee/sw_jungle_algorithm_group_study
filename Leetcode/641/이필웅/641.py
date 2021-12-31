# LeetCode 641. Design Circular Deque
# https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k):
        # 시작 k는 최대 크기
        self._size = 0
        self._front, self._rear = 0, 0
        self._capacity = k
        self._data = [-1] * k

    # deque의 front에 요소(value)를 추가하는 함수.
    # 성공적으로 추가가 완료되면 True값을 리턴한다.
    def insertFront(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self._data[self._front] = value
        else:
            self._front = (self._front - 1) % self._capacity
            self._data[self._front] = value
        self._size += 1
        
        # return type : bool형
        return True

    # deque의 rear에 요소(value)를 추가하는 함수.
    # 성공적으로 추가가 완료되면 True값을 리턴한다.
    def insertLast(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self._data[self._rear] = value
        else:
            self._rear = (self._rear + 1) % self._capacity
            self._data[self._rear] = value
        self._size += 1

        # return type : bool형
        return True

    # deuqe의 front를 지우는 함수.
    # 성공적으로 추가가 완료되면 True값을 리턴한다.
    def deleteFront(self):
        if self.isEmpty():
            return False
        self._data[self._front] = -1
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        if self.isEmpty():
            self._rear = self._front

        # return type : bool형
        return True
    
    # deque의 rear를 지우는 함수.
    # 성공적으로 추가가 완료되면 True값을 리턴한다.
    def deleteLast(self):
        if self.isEmpty():
            return False
        self._data[self._rear] = -1
        self._rear = (self._rear - 1) % self._capacity
        self._size -= 1
        if self.isEmpty():
            self._front = self._rear

        # return type : bool형
        return True

    # deque의 맨앞의 요소를 가져오는 함수
    def getFront(self):
        # return type : int형
        return self._data[self._front]

    # deque의 마지막 요소를 가져오는 함수
    def getRear(self):
        # return type : int형
        return self._data[self._rear]

    # 원형큐가 비었는지 아닌지 체크하는 함수
    def isEmpty(self):
        # return type : bool형
        return self._size == 0

    # 원형큐가 가득찼는지 아닌지 체크하는 함수
    def isFull(self):
        # return type : bool형
        return self._size == self._capacity