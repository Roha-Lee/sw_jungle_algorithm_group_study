# 1. Two sum
[문제 링크](https://leetcode.com/problems/two-sum/)
# 문제 요구 조건 
- 배열에서 두 숫자의 합이 target이 되는 두 인덱스를 구하기 
# 풀이 1
- nums[i]를 Key로 i를 value로 갖는 딕셔너리 선언
- target - nums[i]가 nums[i]에 있는지 확인
    - :bulb: nums와 dictionary에서 in operator의 속도차이에 주의!
- 있다면 두 값의 인덱스 찾아서 반환 
- 딕셔너리에서 동일 키를 갖는 경우 뒤쪽 index를 저장한다.
    - 그래야 앞에서부터 차례로 처리할때 중복된 원소 사용을 방지할 수 있기 때문
# 시간 복잡도 
- dictionary를 사용할 경우 O(N)
    - N개의 원소 O(1)검사
- list를 사용할 경우 이론상 O(N^2)
    - N개의 원소 O(N)검사

# 풀이 2
- two pointer를 이용한 풀이 
- nums[i]를 Key로 i를 value로 갖는 딕셔너리 선언
- 정렬
- 맨 앞과 맨 뒤로 포인터를 두고 두 수의 합이 target보다 작으면 앞의 포인터를 한칸 뒤로 이동하고 target보다 크면 뒤의 포인터를 한칸 앞으로 이동
- 두 포인터가 가리키는 숫자의 인덱스를 반환 
    - 두 숫자가 같은 경우와 같지 않은 경우 나누어서 처리 
# 시간 복잡도 
- 정렬 O(NlogN)
- 투포인터 이용한 값 찾기 O(N)
