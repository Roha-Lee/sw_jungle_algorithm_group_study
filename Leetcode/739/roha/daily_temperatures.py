class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                past_idx, _ = stack.pop()
                answer[past_idx] = idx - past_idx
            stack.append((idx, temp))
        return answer