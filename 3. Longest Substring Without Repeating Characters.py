class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        l = 0
        max_l = 0
        for i, c in enumerate(s):
            if c in s[start:i]:
                start = start + s[start:i].index(c) + 1
                l = i - start + 1
            else:
                l += 1
            max_l = max(max_l,l)
        return max_l
