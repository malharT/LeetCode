class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] != target:
                return -1
            else:
                return 0
        l = len(nums)
        mid = l//2
        if target > nums[mid]:
            i = self.search(nums[mid:], target)
            if i != -1:
                return mid + i
            else:
                return -1
        elif target < nums[mid]:
            i = self.search(nums[:mid], target)
            return i
        else:
            return mid
