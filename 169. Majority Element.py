class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element = nums[0]
        count = 1
        for num in nums[1:]:
            if majority_element == num:
                count += 1
            else:
                count -=1
            if count == 0:
                majority_element = num
                count += 1
        return majority_element
