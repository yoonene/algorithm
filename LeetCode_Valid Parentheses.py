class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c not in table:
                stack.append(c)
            elif not stack or stack.pop() != table[c]:
                return False
        return len(stack) == 0
