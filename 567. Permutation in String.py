class Solution:
    def get_frq_map(self, s1):
        s1_dict = {}
        for c in s1:
            if c in s1_dict:
                s1_dict[c] += 1
            else:
                s1_dict[c] = 1
        return s1_dict

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = self.get_frq_map(s1)
        s2_dict = self.get_frq_map(s2[:len(s1)])
        mismatch = set(s1)
        for c in s1:
            if c in s2_dict:
                if s1_dict[c] == s2_dict[c]:
                    mismatch.discard(c)
        if len(mismatch) == 0:
            return True
        start = 0
        for end in range(len(s1), len(s2)):
            c1 = s2[start]
            s2_dict[c1] -= 1
            c2 = s2[end]
            if c2 in s2_dict:
                s2_dict[c2] += 1
            else:
                s2_dict[c2] = 1
            if c1 in s1_dict:
                if s1_dict[c1] == s2_dict[c1]:
                    mismatch.discard(c1)
                else:
                    mismatch.add(c1)
            if c2 in s1_dict:
                if s1_dict[c2] == s2_dict[c2]:
                    mismatch.discard(c2)
                else:
                    mismatch.add(c2)
            if len(mismatch) == 0:
                return True
            start += 1
        return False
