
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        comb = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in comb:
            if i in s:
                ans += comb[i]
                s = s.replace(i,'')
        for i in s:
            ans += dic[i]
        
        return ans