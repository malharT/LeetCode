class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        solution = [1]*len(nums)
        for i in range(len(nums)):
            solution[i] *= left
            left *= nums[i]
            solution[-i-1] *= right
            right *= nums[-i-1]
        return solution
