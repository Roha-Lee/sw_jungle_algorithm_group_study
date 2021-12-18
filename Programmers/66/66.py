class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp = ''
        for i in digits:
            tmp += str(i)

        tmp = list(map(int, str((int(tmp) +1))))

        return tmp