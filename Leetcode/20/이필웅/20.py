class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                    check.append(i)
            else:
                if len(check) == 0 and (i == ')' or i == '}' or i == ']'):
                    return False
                if i == ')' and check[-1] == '(':
                    check.pop()
                    continue
                if i == '}' and check[-1] == '{':
                    check.pop()
                    continue
                if i == ']' and check[-1] == '[':
                    check.pop()
                    continue
                else:   return False

        if len(check) == 0:
            return True
        else : return False