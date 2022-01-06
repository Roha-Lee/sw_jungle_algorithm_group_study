class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # blocks = [')', '}', ']']
        dict = {
            ')':'(', 
            '}':'{', 
            ']':'['
        }
    
        stack = deque()
        for char in s:
            # char가 여는 괄호이면
            if char not in dict:
                # 스택에 push
                stack.append(char)
            
            else:  # 닫는 괄호가 들어왔을 때
                if stack and dict[char] == stack.pop():     # 스택이 비어있지않고 top의 값이 여는 괄호와 같은 경우 넘어가기.
                    continue
                else:       # 아닌 경우는 False
                    return False
        
        # return True가 아니라 이렇게 작성하면 여는 괄호만 있는 케이스를 고려할 수 있다.(제대로 열고 닫는 괄호가 있는 경우는 stack에 요소가 남는 경우가 없음.)
        return not stack