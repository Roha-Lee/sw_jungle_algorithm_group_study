class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # i를 옮겨가면서 i를 기준으로 양옆으로 뻗쳐가며 팰린드롬 찾기
        def expand(left, right):
            # 문자열의 범위를 넘지 않고 left와 right의 문자가 같은 경우에 반복 시행
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        # 문자열 길이가 1 이하인 경우, 입력받은 문자열 자체가 팰린드롬인 경우 종료
        if len(s) < 2 or s == s[::-1]:
            return s
        result = '' 
        
        for i in range(len(s) - 1):
            # max로 문자열 비교를 할 경우 유니코드로 변환된 숫자 중 큰 값으로 선택
            # 'abcd'와 'abd'를 비교한다면, a와 b는 같으므로 넘어가고 c와 d를 비교해서 유니코드가 더 큰 쪽인 d를 선택
            # 하지만 여기서 max를 고르는 키는 길이이므로 단순 문자열의 길이로 판단.

            # expand(i, i+1)는 팰린드롬이 짝수인 경우,
            # expand(i, i+2)는 팰린드롬이 홀수인 경우를 대비
            # 그 중에서 가장 긴 팰린드롬을 고르기.
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
            
        return result