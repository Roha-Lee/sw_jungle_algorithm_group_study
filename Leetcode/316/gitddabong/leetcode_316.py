class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # 파이썬의 스택과 리스트에는 단순 스택의 연산 이외에 in으로 원소를 찾는 등의 부가적인 편의 기능이 붙어 있다.
        # 하지만 본래 스택에는 없는 연산이므로 책에서는 원소를 찾는 연산을 다른 자료형으로 구현했다 (set)
        
        # 이 문제의 핵심은 중복 제거를 하면서 가능한 한 알파벳 순 정렬
        
        # 이후에 이 알파벳이 또 나올지 아닐지를 판단하기 위한 counter, 결과를 담을 seen 리스트 그리고 stack
        counter, seen, stack = collections.Counter(s), set(), []
        
        for char in s:
            counter[char] -= 1  # 한번 지나친 알파벳은 카운터 제거
            
            if char in seen:    # 중복된 알파벳이 있으면 넘어가기 (여기가 중복 제거 부분)
                continue
                
            while stack and char < stack[-1] and counter[stack[-1]] > 0:    # 스택의 탑의 알파벳이 받아온 char보다 크고 다음에도 또 나올 알파벳이면 (여기가 알파벳 순 정렬 부분)
                seen.remove(stack.pop())    # 지금 빼버리고 다음 기회에 넣기..
                
            stack.append(char)  # char를 스택과 seen에 삽입
            seen.add(char)
        return ''.join(stack)
        
        
        
        # 잘못된 코드
        
#         stack = []
#         for char in s:
#             if char not in stack:   # 문자가 스택에 없는 경우 추가
#                 stack.append(char)
#             elif char in stack and stack[-1] < char:    # 스택에 문자가 있고, 사전순에 맞는 경우
#                 stack.remove(char)
#                 stack.append(char)
#             else:
#                 continue
                
#         return "".join(stack)
        