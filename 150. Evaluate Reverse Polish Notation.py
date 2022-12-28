class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(['+','-','*','/'])
        for c in tokens:
            if c in ops:
                print(c)
                b = stack.pop()
                a = stack.pop()
                result = int(eval(a + c + b))
                stack.append(str(result))
            else:
                stack.append(c)
        return int(stack[0])
