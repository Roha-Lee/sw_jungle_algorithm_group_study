class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join(str(_)for _ in digits)
        num = int(num)
        num = num + 1
        num_list = list(map(int, str(num)))
        return num_list

                
