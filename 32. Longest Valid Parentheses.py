class Solution:
    def calculate_max_score(self, string):
        stack = []
        best_score = 0
        score_at_hold = 0
        i = 0
        for char in string:
            if char == ")":
                if stack:
                    stack.pop()
                    if stack:
                        score_at_hold += 2
                    else:
                        best_score += score_at_hold + 2
                        score_at_hold = 0
                else:
                    return best_score, 0

            else:
                stack.append((char, i))
            i += 1
        last_non_sig_char = 0
        for i in range(len(stack)):
            if i + 1 < len(stack) and stack[i][1] + 1 != stack[i+1][1]:
                last_non_sig_char = stack[i][1]
                break
        if i == len(stack)-1:
            last_non_sig_char = stack[i][1]
        return best_score, last_non_sig_char

    def longestValidParentheses(self, s: str) -> int:
        best_score = 0
        start = 0
        while start < len(s)-1:
            score, last_non_sig_char = self.calculate_max_score(s[start:])
            start += last_non_sig_char + 1
            if score > best_score:
                best_score = score
        return best_score