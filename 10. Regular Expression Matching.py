class Solution:
    def isMatchUnit(self, s, p):
        if len(p) == 2 and p[1] == '*':
            if p == '.*':
                return True
            else:
                if len(s) > 0:
                    if s.count(p[0]) == len(s):
                        return True
                    else:
                        return False
                else:
                    return True
        else:
            if len(p) != len(s):
                return False

            for i in range(len(p)):
                if p[i] != '.' and s[i] != p[i]:
                    return False
            return True

    def isMatch(self, s: str, p: str) -> bool:
        pat = []
        i = 0
        while i < len(p):
            temp = ''
            while i+1 < len(p) and p[i+1] != '*':
                temp += p[i]
                i += 1
            if temp != '':
                pat.append(temp)
            if i+1 == len(p):
                if temp != '':
                    pat[-1] += p[i]
                else:
                    pat.append(p[i])
                i += 1
            else:
                pat.append(p[i:i+2])
                i += 2

        p = pat
        if len(pat) == 1:
            return self.isMatchUnit(s, ''.join(p))
        dp = []
        for _ in range(len(s)+1):
            string_start = []
            for _ in range(len(s)+1):
                string_end = []
                for _ in range(len(p)+1):
                    string_end.append([False]*(len(p)+1))
                string_start.append(string_end)
            dp.append(string_start)

        for se in range(len(s)+1):
            for sm in range(se, -1, -1):
                s2 = s[sm:se]
                for ss in range(sm, -1, -1):
                    s1 = s[ss:sm]
                    for pe in range(2, len(p)+1):
                        for pm in range(pe-1, 0, -1):
                            p2 = p[pm:pe]
                            if len(p2) == 1:
                                dp[sm][se][pm][pe] = self.isMatchUnit(s2, ''.join(p2))
                            if not dp[sm][se][pm][pe]:
                                continue
                            for ps in range(pm-1, -1, -1):
                                p1 = p[ps:pm]
                                if len(p1) == 1:
                                    dp[ss][sm][ps][pm] = self.isMatchUnit(s1, ''.join(p1))
                                
                                dp[ss][se][ps][pe] = (dp[ss][se][ps][pe]
                                                      or (dp[ss][sm][ps][pm]
                                                          and dp[sm][se][pm][pe]))
        return dp[0][len(s)][0][len(p)]
import time
S = Solution()
t = time.time()
print(S.isMatch(s="aab", p="c*a*b*"))
print(time.time() - t)
"aabbcbcacbacaaccacc"
"c*b*b*.*.*.*a*.*"