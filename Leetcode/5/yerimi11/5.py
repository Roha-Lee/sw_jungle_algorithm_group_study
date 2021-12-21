import sys
input = sys.stdin.readline

def longestPalindrome(s):
   #펠린드롬 판별 및 투 포인터 확장
   def expand(left: int, right : int) -> str :
       while left >= 0 and right < len(s) and s[left] == s[right]:
           left -= 1
           right += 1
           # 만약 left 값이 0 일때 회문이라면 left가 -1이되어서 나중에 리턴할때 원하는 0이 아닌 s[0]이 아닌 s[-1]이 리턴되는것을 막기위해. 
           # right는 슬라이싱할때 상관없다.
       return s[left+1 : right]    
   # 해당 사항이 없을 때 빠르게 리턴
   if len(s) < 2 or s == s[::-1] :
       return s

   result = ''
   #슬라이딩 윈도우 우측으로 이동, i가 0인덱스 부터  n-1 인덱스 까지 반복.
   for i in range(len(s)-1) :
       result = max(result, expand(i,i+1), expand(i, i+2), key=len) # 

   return result        

if __name__ == '__main__' :
   s = input().strip()

   print(longestPalindrome(s))  