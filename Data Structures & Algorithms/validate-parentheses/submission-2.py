class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for num in s:
            if num in '({[':
                stack.append(num)
            else:
                if not stack or n[num] != stack[-1]:
                    return False
                    break
                stack.pop()
        return len(stack) == 0