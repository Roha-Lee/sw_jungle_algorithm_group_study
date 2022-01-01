from collections import defaultdict

def solution(enroll, referral, seller, amount):
    name_to_idx = {person:idx for idx, person in enumerate(enroll)}
    graph = defaultdict(str)
    answer = [0] * len(enroll)

    for enr, ref in zip(enroll, referral):
        graph[enr] = ref
    
    for person, num in zip(seller, amount):
        money = num * 100
        curr = person
        while money and not curr == '-':
            tax = money // 10
            answer[name_to_idx[curr]] += money - tax
            curr = graph[curr]
            money = tax
    return answer
        
