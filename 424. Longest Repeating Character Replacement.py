class Solution:
    def add_char(self, freq_map, c):
        if c in freq_map:
            freq_map[c] += 1
        else:
            freq_map[c] = 1

    def rm_char(self, freq_map, c):
        freq_map[c] -= 1

    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        freq_map = {}
        max_freq = 0
        max_len = 0
        for end in range(len(s)):
            c = s[end]
            self.add_char(freq_map, c)
            max_freq = max(max_freq, freq_map[c])
            is_valid = max_freq - end - 1 + start + k
            if is_valid < 0:
                self.rm_char(freq_map, s[start])
                start += 1
            max_len = end + 1 - start
            print(max_freq)
        return max_len
