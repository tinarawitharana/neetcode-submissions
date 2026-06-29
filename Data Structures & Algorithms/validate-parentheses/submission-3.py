class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        matches = {
            ")": "(",
            "]":"[",
            "}":"{"
        }

        for c in s:
            if c in matches:
                if len(stack) == 0 or stack[-1] != matches[c]:
                    return False

                else: 
                    stack.pop()

            else: 
                stack.append(c)

        return not stack