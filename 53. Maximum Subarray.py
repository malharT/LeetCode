class Solution:
    def maxSubArrayLoc(self, nums):
        size = len(nums)
        if size == 1:
            return 0, 1, nums[0]
        mid = size//2
        s1, e1, sum1 = self.maxSubArrayLoc(nums[:mid])
        s2, e2, sum2 = self.maxSubArrayLoc(nums[mid:])
        s2 = s2 + mid
        e2 = e2 + mid        

        temp_sum = 0
        l_sum = float('-inf')
        for i in range(mid, -1, -1):
            temp_sum = temp_sum + nums[i]
            if (temp_sum > l_sum):
                l_sum = temp_sum
                s3=i
        temp_sum = 0
        r_sum = float('-inf')
        for i in range(mid+1, len(nums)):
            temp_sum = temp_sum + nums[i]
            if (temp_sum > r_sum):
                r_sum = temp_sum
                e3=i + 1
        
        if l_sum > 0 and r_sum > 0:
            sum3 = l_sum + r_sum
        elif l_sum > r_sum:
            sum3 = l_sum
            e3 = s3 + 1
        else:
            sum3 = l_sum
            s2= e3 - 1

        if sum3 > sum1 and sum3 > sum2:
            return s3, e3, sum3
        elif sum1 > sum2:
            return s1, e1, sum1
        else:
            return s2, e2, sum2 

    def maxSubArray(self, nums) -> int:
        return self.maxSubArrayLoc(nums)[2]
