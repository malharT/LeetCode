class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        r_count = 0
        for i in range(len(s)):
            if s[i] == 'R':
                r_count += 1
            else:
                r_count -= 1
            if r_count == 0:
                count += 1
        return count