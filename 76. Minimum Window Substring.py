class Solution:
    def add_char(self, m, c):
        if c in m:
            m[c] += 1
        else:
            m[c] = 1

    def createFrqMap(self, s):
        m = defaultdict(int)
        for c in s:
            self.add_char(m,c)
        return m


    def minWindow(self, s: str, t: str) -> str:
        m_t = self.createFrqMap(t)
        start = 0
        m_s = dict()
        mismatch_chars = set(t)
        candidate = ""
        for end in range(len(s)):
            c = s[end]
            self.add_char(m_s, c)
            if m_s[c] == m_t[c]:
                mismatch_chars.discard(c)
            if len(mismatch_chars) == 0:
                c = s[start]
                while m_s[c]-1 >= m_t[c]:
                    start += 1
                    m_s[c] -= 1
                    c = s[start]
                if candidate != "":
                    if len(candidate) > end-start + 1:
                        candidate = s[start:end+1]
                else:
                    candidate = s[start:end+1]
            if candidate != "":
                c = s[start]
                m_s[c] -= 1
                if m_s[c] < m_t[c]:
                    mismatch_chars.add(c)
                start += 1
        return candidate
