class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)
        for day,temp in enumerate(temperatures):
            if len(stack) == 0 or temp <= stack[-1][1]:
                stack.append((day,temp))
            else:
                while len(stack) > 0 and temp > stack[-1][1]:
                    source_day, _ = stack.pop()
                    output[source_day] = day-source_day
                stack.append((day,temp))
        return output