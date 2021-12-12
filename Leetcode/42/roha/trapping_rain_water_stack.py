class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        for c_idx, c_height in enumerate(height):
            last_height = 0

            while stack and stack[-1][1] <= c_height:
                p_idx, p_height = stack.pop()
                water += (min(p_height, c_height) - last_height) * (c_idx - p_idx - 1)
                last_height = p_height
            if stack and stack[-1][1] > c_height:
                water += (min(stack[-1][1], c_height) - last_height) * (c_idx - stack[-1][0] - 1)
            stack.append((c_idx, c_height))
        return water