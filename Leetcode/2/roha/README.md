# 2. Add Two Numbers
[문제 링크](https://leetcode.com/problems/add-two-numbers/)
# 문제 요구 조건 
- 두 숫자를 더하는데, 각 숫자는 역순으로 연결리스트로 표현되어 있다. 더한 결과를 반환하자.(더한 숫자 역시 역순으로 연결된 리스트)
# 제한사항 
- 연결리스트의 노드 개수는 1이상 100이하
- `0<= Node.val <= 9`
- 리스트가 표현하는 숫자는 leading zero를 포함하지 않는다. 

# 풀이 
- Dummy head를 만들어준다.(result)
- carry를 1로 만들어주고 l1과 l2모두 값이 있는 경우에 덧셈을 해서(l1.val + l2.val + carry) 몫을 carry에 넣어주고 나머지를 값으로 하는 노드를 만들어서 result.next에 연결해준다. 
- l1, l2중 하나가 끝난 경우 나머지에 대해서 carry와 더해서 마무리 해주면 된다. 
# 기타 
- 정방향으로 저장되어 있으면?

