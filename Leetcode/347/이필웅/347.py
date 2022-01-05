# LeetCode 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

# k번 이상 등장하는 요소를 추출하라.

import operator
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else: dic[i] += 1
        
        sdict = sorted(dic.items(), key=operator.itemgetter(1),reverse=True)
        ans = []
        for i in range(k):
            ans.append(sdict[i][0])
        
        return ans