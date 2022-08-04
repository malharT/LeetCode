class Solution:
    def findJudge(self, n: int, trust) -> int:
        candidates = set(list(range(1, n + 1)))
        for rel in trust:
            a = rel[0]
            if a in candidates:
                candidates.remove(a)
        if len(candidates) > 1:
            return -1
        if len(candidates) == 0:
            return -1
        judge = candidates.pop()
        non_trusters = set(list(range(1, n + 1)))
        for rel in trust:
            if rel[1] == judge:
                a = rel[0]
                if a in non_trusters: 
                    non_trusters.remove(a)
        if len(non_trusters) > 1:
            return -1
        if len(non_trusters) == 0:
            return -1
        non_trust = non_trusters.pop()
        if non_trust != judge:
            return -1 
        return judge