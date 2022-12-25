class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        idxs = sorted(range(len(nums)), key=lambda x: nums[x])
        nums = sorted(nums)
        i = 0
        k = len(nums) -1
        solutions = []
        sol_set = set()
        while i < k - 1:
            i = 0
            j = k - 1
            while i < j:
                l = nums[i], nums[j], nums[k]
                s = sum(l)
                if s == 0:
                    if tuple(l) not in sol_set:
                        solutions.append(l)
                        sol_set.add(tuple(l))
                if s > 0:
                    j -= 1
                else:
                    i += 1
            k -= 1
        return solutions
