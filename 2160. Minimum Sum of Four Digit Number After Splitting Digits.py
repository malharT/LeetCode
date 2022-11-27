class Solution:
    def minimumSum(self, num: int) -> int:
        num1 = num//1000
        num2 = (num-num1*1000)//100
        num3 = (num-num1*1000-num2*100)//10
        num4 = (num-num1*1000-num2*100-num3*10)
        nums = [num1, num2, num3, num4]
        nums = sorted(nums)
        comb_1 = nums[-1] + nums[0]*100 + nums[1]*10 + nums[2]
        comb_2 = nums[0]*10 + nums[3] + nums[1]*10 + nums[2]
        return min(comb_1, comb_2)