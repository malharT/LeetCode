class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        found = set()
        list_to_return = []
        for item in nums:
            if item in found:
                list_to_return.append(item)
            else:
                found.add(item)
        return list_to_return
