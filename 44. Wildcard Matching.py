class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            if s == "":
                return True
            else:
                return False
        if len(s) == 0:
            if set(p)-set('*'):
                return False
            else:
                return True
        dp = []
        for _ in range(len(p)):
            dp.append([False]*(len(s)))
        if p[0] == '?':
            dp[0][0] = True
        elif p[0] == '*':
            for j in range(len(s)):
                dp[0][j] = True
        else:
            dp[0][0] = p[0] == s[0]
        
        for i in range(1, len(p)):
            chars_in_pat = set(p[:i+1]) - set('*')
            if len(chars_in_pat) == 1:
                if '?' in chars_in_pat or s[0] in chars_in_pat:
                    if p[:i+1].count('*') == i:
                        dp[i][0] = True
            elif len(chars_in_pat) == 0:
                dp[i][0] = True

        i = 1
        for i in range(1,len(p)):
            for j in range(1,len(s)):
                if p[i] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[i] == '*':
                    dp[i][j] = dp[i-1][j-1] or dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1] and p[i] == s[j]
        return dp[len(p)-1][len(s)-1]