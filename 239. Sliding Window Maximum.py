class Solution:
    def add_dque(self, iq, nums, i):
        if len(iq) == 1:
            if nums[iq[0]] > nums[i]:
                iq.append(i)
                return iq
            else:
                return [i]

        mid = len(iq)//2
        if nums[iq[mid]] > nums[i]:
            return iq[:mid] + self.add_dque(iq[mid:], nums, i)
        elif nums[iq[mid]] < nums[i]:
            return self.add_dque(iq[:mid], nums, i)
        else:
            return iq[:mid] + [i]

    def pop_dque(self, iq):
        iq = iq[1:]
        return iq


    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_i = 0
        idque =[]
        output = []
        i = 0
        while i < len(nums):
            if len(idque) > 0 and idque[0] < i - k + 1:
                idque = self.pop_dque(idque)
            idque = self.add_dque(idque, nums, i)
            if i >= k-1:
                output.append(nums[idque[0]])
            i += 1
        return output

