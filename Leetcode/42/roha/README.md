# 42. Trapping Rain Water
[문제 링크](https://leetcode.com/problems/trapping-rain-water/)
# 문제 요구 조건 
- 높이를 나타내는 맵이 주어질때 비가 온 이후 얼마나 많은 양의 비를 저장할 수 있는지 계산하기 
# 제한사항 
- 1 <= heights.length <= 2 * 10^4 
# 풀이
- monotone stack으로 문제 풀었음 
- 높이를 순차적으로 순회하면서 curr_height보다 stack[-1]의 높이가 작으면 스택에서 계속 꺼낸다. 
    - 꺼내면서 물의 높이를 계산
        - 세로: 이전 높이와 현재 높이의 최소값에서 직전 높이를 빼준다.
        - 가로: 현재 인덱스에서 이전 인덱스를 빼고 1을 더 빼준다.
    - 아래 그림 참고 
    ![](https://user-images.githubusercontent.com/82917798/145555791-53ca7bb7-78b0-4f23-86d1-75e842d4ca72.jpeg)
- 마지막을 처리해 주기 위해 조건문을 넣어주었다.
![](https://user-images.githubusercontent.com/82917798/145555902-185ef2fb-7307-4ef2-b7f8-9533710c355b.jpeg)
- 스택에 현재 높이를 넣어준다 
# 시간 복잡도 
- 모든 높이들이 한번씩 stack에 들어갔다 나오기 때문에 O(N)
