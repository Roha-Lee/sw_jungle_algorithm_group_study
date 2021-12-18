class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # digits 내의 숫자들을 다 붙여서 한 숫자로 만들고(자릿수) +1
        number = int(''.join(digits))
        number = str(number + 1)
        results = [i for i in number]
        
        # 에러났지만 문법이나 풀이 아이디어가 맞는지까지만 체크하고싶음 !