class Solution(object):
    def find_median(self, nums):
        if len(nums) > 0:
            if len(nums)%2 == 1:
                med_i = (len(nums)//2,)
            else:
                med_i = len(nums)//2 - 1 , len(nums)//2
            return self.get_median(nums, med_i), med_i
        else:
            return None, None
            

    def get_median(self, nums, index):
        if len(index) == 1:
            return nums[index[0]]
        else:
            return (nums[index[0]] + nums[index[1]])/2
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        if len(nums1) == 1 and len(nums2) == 1:
            med = nums1[0] + nums2[0]
            med = med/2
            return med
        elif len(nums1) == 0:
            med, _ = self.find_median(nums2)
            return med
        elif len(nums2) == 0:
            med, _ = self.find_median(nums1)
            return med

        med_1, med_1_i = self.find_median(nums1)
        med_2, med_2_i = self.find_median(nums2)

        if med_1 == med_2:
            return med_1

        if len(med_1_i) == 2 and len(med_2_i) == 2:
            if nums1[med_1_i[0]] >= nums2[med_2_i[0]] and nums1[med_1_i[1]] <= nums2[med_2_i[1]]:
                return med_1
            elif nums2[med_2_i[0]] >= nums1[med_1_i[0]] and nums2[med_2_i[1]] <= nums1[med_1_i[1]]:
                return med_2

        if len(nums1) == 1 or len(nums2) == 1:
            if len(nums1) == 1:
                value = nums1[0]
                array = nums2
                med = med_2
                med_i = med_2_i
            else:
                value = nums2[0]
                array = nums1
                med = med_1
                med_i = med_1_i
            if len(med_i) == 1:
                if value > med:
                    if value < array[med_i[0]+1]:
                        return (value + med)/2
                    else:
                        return (med + array[med_i[0]+1])/2
                else:
                    if value > array[med_i[0]-1]:
                        return (value + med)/2
                    else:
                        return (med + array[med_i[0]-1])/2
            else:
                if value < array[med_i[1]]:
                    if value <= array[med_i[0]]:
                        return array[med_i[0]]
                    if value > array[med_i[0]]:
                        return value
                else:
                    return array[med_i[1]]
                
        if med_1 > med_2:
            temp = nums1
            nums1 = nums2
            nums2 = temp
            temp_i = med_1_i
            med_1_i = med_2_i
            med_2_i = temp_i
        if len(med_1_i) == 2:
            nums1_start = med_1_i[1]
        else:
            nums1_start = med_1_i[0]
        if len(med_2_i) == 2:
            nums2_end = med_2_i[1]
        else:
            nums2_end = med_2_i[0] + 1

        if len(nums1) > len(nums2):
            nums1_start = len(nums2) - nums2_end
        elif len(nums1) < len(nums2):
            nums2_end = -nums1_start

        return self.findMedianSortedArrays(nums1[nums1_start:],
                                           nums2[:nums2_end])
        
S = Solution()
print(S.findMedianSortedArrays([1,2,3,4], [5,6,7,8]))