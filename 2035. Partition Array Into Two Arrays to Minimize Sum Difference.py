from itertools import combinations
import math
class Solution:
    def find_index_for(self, arr, num):
        l = len(arr)
        if l == 1:
            if num <= arr[0]:
                return 0
            else:
                return 1
        if l == 0:
            return 0
        mid = l//2
        if arr[mid] > num:
            return self.find_index_for(arr[:mid], num)
        elif arr[mid] == num:
            return mid
        else:
            return mid + 1 + self.find_index_for(arr[mid+1:], num)

    def add_num_to_list(self, nums, num):
        i = self.find_index_for(nums, num)
        nums.insert(i, num)
        return nums

    def calcSubArray(self, nums):
        x = []
        for i in range(len(nums)+1):
            x.append([])
            for c in combinations(nums, i):
                x[i].append(sum(c))
            x[i] = sorted(x[i])
        return x

    def findClosestNum(self, arr, num):
        l = len(arr)
        i = self.find_index_for(arr, num)
        if i == 0:
            return arr[0], 0
        if i == l:
            return arr[l-1], l-1
        else:
            if abs(arr[i] - num) < abs(arr[i-1] - num):
                return arr[i], i
            else:
                return arr[i-1], i-1

    def minimumDifference(self, nums):
        l = int(len(nums)/2)
        total_sum =sum(nums) 
        best_sum =total_sum/2
        sums_in_first_half = self.calcSubArray(nums[:l])
        sums_in_second_half = self.calcSubArray(nums[l:])
        min_diff_sum = sum(nums[:l])
        t1 = time.time()
        for i in range(int(l)):
            _, upper_bound = self.findClosestNum(sums_in_second_half[l-i], best_sum - sums_in_first_half[i][-1])
            sums_in_second_half[l-i] = sums_in_second_half[l-i][upper_bound:]
            past_idx = len(sums_in_second_half[l-i])
            limit = max(1, int(math.log2(past_idx)))
            for _, part_sum in enumerate(sums_in_first_half[i]):
                required_sum = best_sum - part_sum 
                idx_1 = max(0, past_idx-limit)
                if (sums_in_second_half[l-i][idx_1] < required_sum):
                    other_part_sum, past_idx = self.findClosestNum(sums_in_second_half[l-i][idx_1:past_idx+1], best_sum - part_sum)
                    past_idx += idx_1
                else:
                    other_part_sum, past_idx = self.findClosestNum(sums_in_second_half[l-i][:past_idx+1], best_sum - part_sum)
                if abs(min_diff_sum - best_sum) > abs(part_sum + other_part_sum - best_sum):
                    min_diff_sum = part_sum + other_part_sum
                curr = abs(part_sum + other_part_sum - best_sum)
        print(time.time() - t1)
        return abs(total_sum - 2*min_diff_sum)

import time
S = Solution()
t1 = time.time()
print(S.minimumDifference([1038,-7559,-6091,7459,3436,-906,-6035,1180,2831,8080,-4710,8853,615,-2247,9763,2561,-683,-2793,6497,8510,3892,758,5570,2652,-4599,1259,-1439,4846,-731,-4190]))
print(time.time() - t1)