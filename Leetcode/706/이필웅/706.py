# LeetCode 706. Design HashMap
# https://leetcode.com/problems/design-hashmap/

# 해쉬맵 구현 문제

import collections

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        
class MyHashMap:
    # 초기화
    def __init__(self):
        self.size = 999
        self.table = collections.defaultdict(ListNode)

    # 삽입        
    def put(self, key: int, value: int) -> None:    # 키 값 해시맵에 삽입. 존재하면 업데이트
        index = key % self.size
        
        # value값을 비교하는 이유 : defaultdict는 없는 값을 참조할 경우 생성하기 때문
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        # 인덱스에 노드가 존재하는 경우 연결리스트 처리 방식
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key,value)

    # 조회
    def get(self, key: int) -> int: # 키 값 반환, 없으면 -1 리턴
        index = key % self.size
        if self.table[index].value is None:
            return -1
        
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        
        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
