from collections import Counter
def solution(participant, completion):
    cntr_part = Counter(participant)
    cntr_comp = Counter(completion)
    
    for person in participant:
        if cntr_part[person] - cntr_comp[person] == 1:
            return person
    