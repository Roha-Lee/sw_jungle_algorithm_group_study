# 21. Merge two sorted lists
[문제 링크](https://leetcode.com/problems/merge-two-sorted-lists/)
# 문제 요구 조건 
- 두 개의 정렬된 리스트가 있을 때 하나로 합쳐서 정렬된 리스트를 만들기
# 제한사항 
- 각 리스트의 노드 개수는 0이상 50이하
- -100 <= Node.val <= 100
- list1과 list2는 오름차순으로 정렬
# 풀이 
1. dummy node를 하나 만들고 시작한다. 
    - head부분의 처리를 신경쓰지 않아도 된다. 
2. l1과 l2가 모두 None이 아닌 동안 반복문을 돌면서 l1의 값이 더 작으면 l1노드를 연결, 반대의 경우 l2노드를 연결한다. 
3. 한쪽이 None이 된 경우 다른 한쪽을 리스트의 나머지가 되도록 연결해준다.
4. dummy node 다음 노드를 반환한다.  
# 시간 복잡도 
- l1의 길이를 N, l2의 길이를 M이라 할때 O(N+M)