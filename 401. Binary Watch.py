class Solution:
    def count_1s(self, num):
        c = 0
        while num:
            c += 1
            num = num & (num-1)
        return c

    def get_possible_hours(self, num):
        nums = []
        for i in range(12):
            if self.count_1s == num:
                nums.append(i)
        return nums

    def get_possible_mins(self, num):
        nums = []
        for i in range(59):
            if self.count_1s == num:
                nums.append(i)
        return nums
                
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        max_pos_led_h = min(3, turnedOn)
        times = []
        hours_lookup = {0:[], 1:[], 2:[], 3:[]}
        mins_lookup = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
        for i in range(12):
            hours_lookup[self.count_1s(i)].append(i)

        for i in range(60):
            mins_lookup[self.count_1s(i)].append(i)

        for h in range(max_pos_led_h+1):
            ctr = turnedOn - h
            if ctr > 6:
                continue
            for hr in hours_lookup[h]:
                hr = str(hr)
                for mn in mins_lookup[ctr]:
                    if mn < 10:
                        mn = '0' + str(mn)
                    else:
                        mn = str(mn)
                    times.append(hr+':'+mn)
        return times
