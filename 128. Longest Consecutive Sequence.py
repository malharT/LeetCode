from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        winner_len = 0
        forward = {}
        backward = {}
        for num in nums:
            if num not in forward and num not in backward:
                l = [num]
                if num+1 not in forward and num-1 not in backward:
                    forward[num+1] = l
                    backward[num-1] = l
                winner_len = max(winner_len, 1)
            if num in forward and num not in backward:
                if num+1 in forward and len(forward[num]) + 1 < len(forward[num+1]):
                    continue
                else:
                    forward[num+1] = forward[num]
                    forward[num+1].append(num)
                    del forward[num]
                    winner_len = max(winner_len, len(forward[num+1]))
                
            if num in backward and num not in forward:
                if num-1 in backward and len(backward[num]) + 1 < len(backward[num-1]):
                    continue
                else:
                    backward[num-1] = backward[num]
                    backward[num-1].insert(0, num)
                    del backward[num]
                winner_len = max(winner_len, len(backward[num-1]))
            if num in backward and num in forward:
                new_l = forward[num] + [num] + backward[num]
                if new_l[-1]+1 in forward and len(new_l) < len(forward[new_l[-1]+1]):
                    pass
                else:
                    forward[new_l[-1]+1] = new_l
                    del forward[num]
                if new_l[0]-1 in backward and len(new_l) < len(backward[new_l[0]-1]):
                    pass
                else:
                    backward[new_l[0]-1] = new_l
                    del backward[num]
                winner_len = max(winner_len, len(new_l))
        return winner_len
