class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        hi = len(nums)
        k = 0
        while hi > low:
            mid = low + (hi-low)//2
            if nums[mid] > nums[0]:
                low = mid + 1
            elif nums[mid] < nums[0]:
                hi = mid
                k = mid
            else:
                k = mid
                break
        if target > nums[0]:
            low = 0
            if k > 0:
                hi = k
            else:
                hi = len(nums)
        elif target < nums[0]:
            low = k
            hi = len(nums)
        else:
            return 0
        ans = -1
        while hi > low:
            mid = low + (hi-low)//2
            if nums[mid] > target:
                hi = mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return ans
