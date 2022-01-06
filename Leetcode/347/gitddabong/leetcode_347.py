class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Counter 모듈로 원소들의 개수를 카운트
        # set으로 nums의 중복을 제거해주고
        # 카운트가 제일 높은 순으로 정렬해주고 다시 역순으로 정렬해준다
        # 그리고 앞에서부터 k개 만큼 출력
        
        counts = collections.Counter(nums)
        nums_set = list(set(nums))
        result = []
        
        nums_set.sort(key=lambda x : counts[x], reverse=True)
        for i in range(k):
            result.append(nums_set[i])
            
        return result


        # 힙을 사용한 코드 책 풀이
        
#         freqs = collections.Counter(nums)
#         freqs_heap = []
        
#         # 힙에 음수로 삽입 (최대 힙으로 사용)
#         for f in freqs:
#             heapq.heappush(freqs_heap, (-freqs[f], f))
            
#         topk = list()
#         # k번 만큼 추출, 최소 힙(Min Heap)이므로 가장 작은 음수 순을 추출
#         for _ in range(k):
#             topk.append(heapq.heappop(freqs_heap)[1])
            
#         return topk