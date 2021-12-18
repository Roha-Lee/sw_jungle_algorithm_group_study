class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 로마자 숫자는 큰수 -> 작은수 순서로 적는다
        # 4는 5-1이라 로마자 1,5를 적는다. 9도 마찬가지로 로마자 10,1로 적는다
        # 마찬가지로 10, 100 단위에서도 적용. 40은 로마자 50,10로 적고, 400은 로마자 500,100으로 적는다
        
        roman = [I, V, X, L, C, D, M]
        
        1 = I
        5 = V
        10 = X
        50 = L
        100 = C
        500 = D
        1000 = M # 이게 맞나?
        
        # s입력값과 roman리스트 내의 문자와 비교
        s = s.split()
        
        while s[i] == roman: # s의 원소가 roman 리스트 내에 있는지 찾고싶은데 이 문법이 아닌 것 같음
#             # roman 숫자 계산 / 같은 로마자가 여러개일때를 나누고 싶은데 다시짜야할듯
#             for i in roman:
#                 if len(i) = 0:
#                     continue

#                 elif len(i) <= 3:
#                     cal = i * len(s)

#                 else : # I가 4개 이상이면 을 하고싶었는데 완전 잘못된듯 답보고 갈아엎어야할듯
#                     cal = (i+1) + (i-1)
                