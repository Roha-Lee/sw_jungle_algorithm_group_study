from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = defaultdict(list)
        for word in strs:  
            cntr = Counter(word)
            group_dict[tuple(sorted(cntr.items()))].append(word)
        return list(group_dict.values())