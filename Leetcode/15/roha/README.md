# 15. 3 Sum
[문제 링크](https://leetcode.com/problems/3sum/)
# 문제 요구 조건 
- nums에 있는 숫자 3개를 더해서 0이 되는 모든 triplet을 구하자
# 제한사항 
- `0 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`
# 풀이 
1. 주어진 숫자를 정렬한다. 
    - 계수정렬을 할까 했는데, 그냥 정렬을 하는 편이 더 이득이다. 
2. 왼쪽 끝부터 start를 한칸씩 오른쪽으로 이동한다. 
    - end를 맨 끝부터 한칸씩 왼쪽으로 이동시키면서 start + 1까지 이동시키면서 start위치와 end위치의 nums를 더한다. 
    - 부호를 반대로 하여 남은 하나의 수를 구한다. 
    - dictionary의 in operation을 통해 start + 1부터 end - 1사이의 index에 대해서 남은 하나의 수가 있는지 확인한다. 
3. 불필요한 연산을 제거하기 위해 start와 start-1값이 같으면 넘어가고 e_ptr과 e_ptr+1이 같으면 넘어간다. 