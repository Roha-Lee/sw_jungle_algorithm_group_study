class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # 딕셔너리 형태. {'key'검색, : 'value'}
        table = {')': '(', 
                 '}': '{',
                 ']': '[' }
        
        for character in s:
            # 입력받은 문자가 테이블에 없으면 스택에 더해준다
            if character not in table:
                stack.append(character)
            # 스택이 비어있거나 테이블에 문자열 키 검색 후 나오는 값이 스택에 들어있다가 빠져야하는 값이랑 같지 않으면
            elif not stack or table[character] != stack.pop():
                return False
        return len(stack) == 0
        # 그냥 return True 하면 '(]' 에서도 true가 나온다.
        # 스택이 비어있을 때만 true(?)

        # 스택연산 push, pop : O(1)에 동작.