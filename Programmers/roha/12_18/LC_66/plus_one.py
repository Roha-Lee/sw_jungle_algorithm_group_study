class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = 1
        for digit in reversed(digits):
            if digit + carry > 9:
                digit -= 9 
                carry = 1
            else:
                digit += carry
                carry = 0       
            result.append(digit)
        if carry:
            result.append(carry)
        return reversed(result)
                
            
            