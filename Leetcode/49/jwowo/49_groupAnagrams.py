from collections import Counter
# 정렬된 단어를 키 값으로하는 해쉬 테이블
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for word in strs:
            sorted_key = ''.join(sorted(word))
            if sorted_key not in anagrams.keys():
                anagrams[sorted_key] = []
            
            anagrams[sorted_key].append(word) 
        
        return list(anagrams.values())