class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        english, digit = [], [] 
        
        for log in logs:
            if log.split()[1].isnumeric():
                digit.append(log)
            else:
                english.append(log)
                
        english.sort(key = lambda x : (x.split()[1:], x.split()[0]))
        
        return english + digit