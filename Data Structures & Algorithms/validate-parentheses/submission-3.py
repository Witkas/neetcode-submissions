class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if stack == []:
                    return False
                last = stack.pop()
                if (last == '(' and c != ')') or (last == '{' and c != '}') or (last == '[' and c != ']'):
                    return False
        if stack == []:
            return True
        else:
            return False
        