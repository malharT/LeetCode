class Solution:
    def calculate_third_repeating_char(self, password):
        third_repeating_char_pos = []
        prev_char = password[0]
        i = 0
        seq_start = None
        for j in range(1, len(password)):
            char = password[j]
            if prev_char == char:
                i += 1
            if i > 1 and seq_start is  None:
                seq_start = j
            if i > 1 and (prev_char != char or (j + 1)== len(password)):
                third_repeating_char_pos.append((seq_start, prev_char, i-2))
                seq_start = None
            if prev_char != char:
                i = 0
            prev_char = char
        return third_repeating_char_pos
    def char_type(self, char):
        if char in self.set_nums:
            return 'num'
        if char in self.set_lowercase:
            return 'low'
        if char in self.set_uppercase:
            return 'up'
        else:
            return 'spl'
    def strongPasswordChecker(self, password: str) -> int:
        self.set_nums = {'0', '1', '2', '3', '4',
                         '5', '6', '7', '8', '9'}
        self.set_lowercase = {'a', 'b', 'c', 'd',
                              'e', 'f', 'g', 'h',
                              'i', 'j', 'k', 'l',
                              'm', 'n', 'o', 'p',
                              'q', 'r', 's', 't',
                              'u', 'v', 'w', 'x',
                              'y', 'z'}
        self.set_uppercase = set()
        for item in self.set_lowercase:
            self.set_uppercase.add(item.upper())

        lacks_char = max(0, 6 - len(password))
        exceeds_chars = max(0, len(password) - 20)
        lacks_lower_case = set(password).intersection(self.set_lowercase) == set()
        lacks_upper_case = set(password).intersection(self.set_uppercase) == set()
        lacks_nums = set(password).intersection(self.set_nums) == set()
        missing_cat = int(lacks_lower_case) + int(lacks_upper_case) + int(lacks_nums)

        third_repeating_char_pos = self.calculate_third_repeating_char(password)
        steps_to_repair = 0
        pwd_len = len(password)
        while lacks_char or missing_cat or exceeds_chars or third_repeating_char_pos:
            steps_to_repair += 1
            if third_repeating_char_pos and lacks_char and missing_cat:
                pos, char, l = third_repeating_char_pos.pop(0)
                if l>2:
                    pos += 1
                    l -= 3
                    third_repeating_char_pos.insert(0, (pos, char, l))
                missing_cat -= 1
                lacks_char -= 1
            elif third_repeating_char_pos and lacks_char:
                pos, char, l = third_repeating_char_pos.pop(0)
                if l>2:
                    pos += 1
                    l -= 3
                    third_repeating_char_pos.insert(0, (pos, char, l))
                lacks_char -= 1
            elif lacks_char and missing_cat:
                missing_cat -= 1
                lacks_char -= 1
            elif third_repeating_char_pos and exceeds_chars:
                i = 0
                best_removal = None
                best_l = 3
                for pos, char, l in third_repeating_char_pos:
                    if l%3 < best_l:
                        best_l = l%3
                        best_removal = i
                    i += 1
                pos, char, l = third_repeating_char_pos.pop(best_removal)
                password = password[:pos] + '' + password[pos+1:]
                if l > 0:
                    l -= 1
                    third_repeating_char_pos.insert(best_removal, (pos, char, l))
                exceeds_chars -= 1
            elif third_repeating_char_pos and missing_cat:
                pos, char, l = third_repeating_char_pos.pop(0)
                if l>2:
                    pos += 1
                    l -= 3
                    third_repeating_char_pos.insert(0, (pos, char, l))
                missing_cat -= 1
            elif third_repeating_char_pos:
                pos, char, l = third_repeating_char_pos.pop(0)
                if l>2:
                    pos += 1
                    l -= 3
                    third_repeating_char_pos.insert(0, (pos, char, l))
            elif lacks_char:
                lacks_char -= 1
            elif missing_cat:
                missing_cat -=1
            elif exceeds_chars:
                exceeds_chars -= 1
        return steps_to_repair

