from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        jumps = 0
        while i < len(nums)-1:
            max_jump = 0
            if i + nums[i] + 1 >= len(nums):
                jumps += 1
                break
            for idx in range(i+1, i + nums[i] + 1):
                jump = idx+nums[idx]
                if jump > max_jump:
                    max_jump = max(jump, max_jump)
                    i = idx
            jumps += 1
        return jumps

S = Solution()
print(S.jump([2,3,1]))