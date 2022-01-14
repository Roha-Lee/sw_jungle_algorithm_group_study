class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap(object):

    # 초기화
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)  # 테이블에 없는 값 조회 시 바로 필드를 추가할 수 있는 defaultdict로 구현
        

    # 삽입
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # 해시 함수 포함.
        index = key % self.size
        
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        # 인덱스에 노드가 존재하는 경우 연결리스트 처리
        p = self.table[index]       # p : 해시 함수를 써서 들어간 링크드리스트의 첫 노드
        while p:
            if p.key == key:        # 같은 키 값을 가지는 노드가 있다면 값을 업데이트 후 종료
                p.value = value
                return
            if p.next is None:      # 링크드리스트의 끝 노드까지 서치
                break
            p = p.next
        p.next = ListNode(key, value)   # 현재 노드의 next에 새로운 노드 삽입
        
    # 조회
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # 해시 함수 포함.
        index = key % self.size
        
        if self.table[index].value is None:     # 값이 없으면 -1
            return -1
        
        # 노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:        # 같은 키 값의 노드를 찾으면 값 반환
                return p.value  
            p = p.next
        return -1   # 다 뒤져봤는데 없으면 -1

    # 삭제
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        # 해시 함수 포함
        index = key % self.size
        if self.table[index].value is None:     # 찾는 값이 없으면 종료
            return
        
        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next    # 현재 노드의 다음 노드가 없으면 빈 노드 하나 넣고 아니면 다음 노드를 현재 위치에 삽입
            return
        
        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next      # 앞뒷노드 연결만 해주고 마무리
                return
            prev, p = p, p.next     # 포인터 한칸씩 전진
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)