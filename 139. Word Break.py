class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        trie = {}
        for word in wordDict:
            sub_trie = trie
            for c in word:
                if c not in sub_trie:
                    sub_trie[c] = {}
                sub_trie = sub_trie[c]
            sub_trie['#'] = None
        if s[0] not in trie:
            return False
        sub_tries = [trie]
        i = 0
        while i < len(s) and sub_tries:
            c = s[i]
            j = 0
            append_trie = False
            while j < len(sub_tries):
                sub_trie = sub_tries[j]
                if c in sub_trie:
                    sub_trie = sub_trie[c]
                    sub_tries[j] = sub_trie
                    if '#' in sub_trie:
                        if i == (len(s) - 1):
                            return True
                        else:
                            append_trie = True
                else:
                    sub_tries.pop(j)
                    j -= 1
                j += 1
            if append_trie:
                sub_tries.append(trie)
            i += 1
        return False