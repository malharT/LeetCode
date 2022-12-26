class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i = 0
        for num in nums:
            if target-num in seen:
                return seen[target-num], i
            else:
                seen[num] = i
            i += 1