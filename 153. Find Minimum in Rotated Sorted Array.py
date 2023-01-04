class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        hi = len(nums)
        ans = 0
        while hi > low:
            mid = low + (hi-low)//2
            if nums[mid] > nums[0]:
                low = mid + 1
            elif nums[mid] < nums[0]:
                ans = mid
                hi = mid
            else:
                if nums[ans] > nums[mid]:
                    ans = mid
                break
        return nums[ans]
