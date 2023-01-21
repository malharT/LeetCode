class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t = nums[0]
        h = nums[nums[0]]
        while t!=h:
            t = nums[t]
            h = nums[nums[h]]
        t = 0
        while t!=h:
            t = nums[t]
            h = nums[h]
        return h