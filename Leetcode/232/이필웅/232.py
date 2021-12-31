# LeetCode 232.Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/

# 스택을 이용하여 큐를 구현하는 문제.
# 스택을 2개사용한다. -> 하나에서 뽑아서 넣는다고 가정하면 무한루프발생.

class MyQueue:
    
    # 하나의 큐만을 이용하면 무한루프 발생.(한개에서 한개뽑아다 삽입하면 계속해서 뽑아다가 삽입하므로)
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek() 
        return self.output.pop()

    def peek(self) -> int:
        # output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

        return self.output[-1] # 스택의 맨 위이므로.

    def empty(self) -> bool:
        return self.input == [] and self.output == []        
