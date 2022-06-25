class Solution:
    def findSubstring(self, s: str, words: list) -> list:
        words_id = dict()
        i = 0
        for word in words:
            if word in words_id:
                words_id[word].append(i)
            else:
                words_id[word] = [i]
            i += 1
        len_of_word = len(words[0])
        words_window = []
        solutions = []
        i = 0
        for i in range(len_of_word):
            words_window.append([-1]*len(words))
        for j in range(len(s)):
            seq_id = j%len_of_word
            w_id = words_window[seq_id].pop(0)
            word = s[j:j+len_of_word]
            if word in words_id:
                w_ids = words_id[word]
                found_word = False
                for i in range(len(w_ids)):
                    w_id = w_ids[i]
                    if w_id in words_window[seq_id]:
                        continue
                    if w_id not in words_window[seq_id]:
                        words_window[seq_id].append(w_id)
                        w_ids.pop(i)
                        w_ids.append(w_id)
                        found_word = True
                        break
                if not found_word:
                    w_id = w_ids.pop(0)
                    w_ids.append(w_id)
                    words_window[seq_id].append(w_id)

            else:
                words_window[seq_id].append(-1)
            words_set = set(words_window[seq_id])
            if len(words_set) == len(words) and -1 not in words_set:
                sol = j - len_of_word*(len(words)-1)
                solutions.append(sol)

        return solutions