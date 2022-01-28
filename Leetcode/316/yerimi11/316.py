class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 중복된 문자를 제거하고 사전순으로 정렬해라
        
        # 리스트에 append 하고 if 같으면 pop
        # 사전식정렬 -> acbd, adbc => 1. acbd 2. adbc (2번째 문자 기준)
        
        # 문자열 string을 list로
        # 중복 문자 제거 -> 스택으로!? 리스트 스택에 넣는 과정에서 같으면 안넣고 다르면 어펜드
        
        # counter -> a:1, b:2, c:4, d:1 알파벳 갯수 세어줌
        counter = collections.Counter(s)
        seen = set()    # set() = 중복제거 / seen => " " 빈 set 만들어짐
        stack = []
        
        for char in s:
            counter[char] -= 1 # a:1, b:2, c:4->3으로 감소, d:1
            if char in seen:
                continue
            # 뒤에 붙일 문자가 남아있다면(사전순으로 더 큰 알파벳인지 판단 ex:a < b이면 a가 앞에 오는게 이득이니) 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop()) # 왼쪽부터 지움
            stack.append(char)
            seen.add(char) # set()에서의 append함수 => add
        return ''.join(stack)
            
    
        List in : worst O(n)  // 둘 같은 in operation 이지만
        Set in : .. -> hash collision 확률적으로 낮음. 보통은 O(1)가 나옴.