class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits))) + 1
        answer = list(str(num))
        
        return answer