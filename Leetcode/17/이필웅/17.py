# LeetCode 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# 번호 조합을 이용하여 문자열 Combinations의 리스트를 반환하는 문제

# Runtime : 62ms (5.39%)
# Memory Usage : 14.3MB (33.58%)

from itertools import product
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
    
        if digits == "":
            return []
        
        digits = map(int,list(digits))
        
        bucket = []
        for i in digits:
            bucket.append(dic[i])
        
        comb_bucket = list(product(*bucket))
        
        ans = []
        for i in comb_bucket:
            ans.append(''.join(i))

        return ans




#[s + c for s in prev for c in additional]
# s+c => 표현식, s 항목 in 리스트 

# 두번째 풀이
# 재귀를 함수로 이용한 더 빠른 방법.

# Runtime : 37ms (71.52%)
# Memory Usage : 14.3MB (33.58%)

    def letterCombinations2(self, digits):
            mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
            if len(digits) == 0:
                return []
            if len(digits) == 1:
                return list(mapping[digits[0]])
            prev = self.letterCombinations2(digits[:-1])
            additional = mapping[digits[-1]]

            return [s + c for s in prev for c in additional]

a = Solution().letterCombinations2("222")

print(a)