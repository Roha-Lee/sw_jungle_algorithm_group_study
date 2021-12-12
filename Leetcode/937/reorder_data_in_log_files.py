class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []
        for log in logs:
            log_split = log.split()
            if log_split[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append((log_split[1:], log_split[0]))
                letter_logs.append(log)
        letter_logs = [" ".join([key, *contents]) for contents, key in letter_logs]
        return letter_logs + digit_logs
        
            
        