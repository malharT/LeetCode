class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack = stack[:-1]
                    continue
            elif c == "]":
                if len(stack) > 0 and stack[-1] == "[":
                    stack = stack[:-1]
                    continue
            elif c == "}":
                if len(stack) > 0 and stack[-1] == "{":
                    stack = stack[:-1]
                    continue
            stack.append(c)
        return len(stack) == 0
