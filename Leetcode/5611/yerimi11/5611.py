class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
        # 정렬된 상태에서 오름차순으로 인접 요소 페어를 만들면, 가장 큰 a1과 a2페어를 만들 수 있고 이 페어 합이 곧 최대 합이 된다
        sum = 0
        pair = []
        nums.sort()
        
        for n in nums:
            # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
                
        return sum