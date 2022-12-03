class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_1 = max(nums[0], nums[1])
        max_2 = min(nums[0], nums[1])
        for i in range(2, len(nums)):
            if max_1 <= nums[i]:
                max_2 = max_1
                max_1 = nums[i]
            elif max_2 <= nums[i]:
                max_2 = nums[i]
        return (max_1-1)*(max_2-1)
