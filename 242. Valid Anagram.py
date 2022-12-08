class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for char in t:
            if char not in d:
                d[char] = 0
            d[char] += 1
        for char in s:
            if char in d:
                d[char] -= 1
            else:
                return False
            if d[char] == 0:
                del d[char]
        return not d
