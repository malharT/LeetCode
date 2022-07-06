class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [None]*len(s)
        dp[0] = [(0, 0)]
        if len(s) == 1:
            return s

        if s[0] == s[1]:
            dp[1] = [(0, 1)]
            max_len = 2
            sol_start = 0
            sol_end = 2
        else:
            dp[1] = [(1, 1)]
            max_len = 1
            sol_start = 1
            sol_end = 2

        for end in range(2, len(s)):
            new_len = 0
            new_start = None
            new_end = None
            dp[end] = []
            for cur_s, cur_e in dp[end-1]:
                if cur_s-1 >= 0:
                    if s[cur_s -1] == s[end]:
                        dp[end].append((cur_s -1, end))
                        if end - cur_s + 2> new_len:
                            new_len = end - cur_s + 2
                            new_start = cur_s - 1
                            new_end = end 
            if s[end] == s[end-2]:
                dp[end].append((end-2, end))
                if 3 > new_len:
                    new_len = 3
                    new_start = end - 2
                    new_end = end
            if s[end] == s[end-1]:
                 dp[end].append((end-1, end))
                 if 2 > new_len:
                    new_len = 2
                    new_start = end - 1
                    new_end = end
            dp[end].append((end, end))
            if 1 > new_len:
                new_len = 1
                new_start = end - 1
                new_end = end
            if new_len > max_len:
                max_len = new_len
                sol_start = new_start
                sol_end = new_end + 1

        return s[sol_start:sol_end]

S = Solution()
import time
t1 = time.time()
print(S.longestPalindrome("aaaa"))
print(time.time()-t1)