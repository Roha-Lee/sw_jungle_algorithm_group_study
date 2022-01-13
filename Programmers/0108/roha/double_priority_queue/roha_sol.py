from heapq import heappush, heappop
def solution(operations):
    min_heap, max_heap = [], []
    num_elem, del_elem = 0, 0
    
    for operation in operations:
        op, val = operation.split()
        val = int(val)
        if num_elem == del_elem:
            min_heap = []
            max_heap = []
        if op.lower() == 'i':
            heappush(min_heap, val)
            heappush(max_heap, -val)
            num_elem += 1
        elif op.lower() == 'd':
            if num_elem <= del_elem:
                continue
            if val == -1:
                heappop(min_heap)
            else:
                heappop(max_heap)
            del_elem += 1
        
    if num_elem == del_elem:
        return [0, 0]
    return [-max_heap[0], min_heap[0]]