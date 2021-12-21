class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        
        for i in range(length):
            digits[i] = str(digits[i])

        _string = "".join(digits)
        num = int(_string) + 1

        new_digits = list(str(num))

        for i in range(length):
            new_digits[i] = int(new_digits[i])
            
        return new_digits
            