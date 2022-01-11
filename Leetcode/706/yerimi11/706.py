# 연결리스트 클래스 정의
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap(object):
    # 해시맵 - 개별 체이닝 방식
    
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode) # 존재하지 않는 키를 조회할 경우를 위해 defaultdict 사용

    def put(self, key, value): # 삽입
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # 같은 것을 가리키는 경우 거르기 위함
        index = key % self.size
        
        # 인덱스에 해당되는 노드가 없다면 삽입 후 연결리스트 처리 할 필요 없이 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        # 인덱스에 노드가 존재하는 경우 연결리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break   # 반복문 종료
            p = p.next  # 다음 노드로 go
        p.next = ListNode(key, value) # 다음 자리에 빈 노드 생성
        

    def get(self, key): # 조회
        """
        :type key: int
        :rtype: int
        """
        # 찾는 위치에 값이 없으면 -1 리턴
        index = key % self.size
        if self.table[index].value is None:
            return -1
        
        # 노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
        

    def remove(self, key): # 삭제
        """
        :type key: int
        :rtype: None
        """
        index = key % self.size
        if self.table[index].value is None:
            return
        
        # 인덱스의 첫번째 노드일 때 삭제처리
        p = self.table[index]
        if p.key == key: # 지울 key
            # 다음 값이 None이면 return ListNode()로 빈 노드 만들고, 아니면 지웠다 치고 다음 노드 리턴
            # 빈 노드 생성 이유 : 다음 값이 없다는건 얘가 첫번째라는거고, 첫번째에 빈 노드 덮어씌우는 걸로 삭제처리함. 다른 방법도 있지 않을까?
            self.table[index] = ListNode() if p.next is None else p.next
        
        # 연결리스트 노드 삭제 -> 연결 끊어버림
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)