class Solution:
    def removeDuplicates(self, nums: list) -> int:
        if len(nums) == 1:
            return nums
        i = 1
        j = 1
        while i < len(nums):
            if nums[i-1] != nums[i]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return nums
S = Solution()
print(S.removeDuplicates([1, 2, 2]))