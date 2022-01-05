from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cntr = Counter(stones)
        jewels = set(jewels)
        result = 0
        for letter in list(jewels):
            result += cntr[letter]
        return result
            