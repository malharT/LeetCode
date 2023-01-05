class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp
        
        if len(nums1) == 0:
            mid = len(nums2)//2
            if len(nums2)%2 == 0:
                return(nums2[mid-1] + nums2[mid])/2
            else:
                return nums2[mid]

        l = 0
        h = len(nums1)
        full_len = len(nums1) + len(nums2)
        mid = full_len//2
        while True:
            split1_i = l + (h-l)//2
            split2_i = mid - split1_i
            if (split1_i != 0 and split2_i != len(nums2)
                and nums1[split1_i-1] > nums2[split2_i]):
                h = split1_i
                continue
            elif (split1_i != len(nums1) and split2_i != 0
                and nums1[split1_i] < nums2[split2_i-1]):
                l = split1_i + 1
                continue
            else:
                if full_len%2 == 1:
                    if (split1_i == len(nums1)):
                        return nums2[split2_i]
                    elif (split2_i == len(nums2)):
                        return nums1[split1_i]
                    return min(nums1[split1_i], nums2[split2_i])
                else:
                    if split1_i == 0:
                        l = nums2[split2_i-1]
                    elif split2_i == 0:
                        l = nums1[split1_i-1]
                    else:
                        l = max(nums1[split1_i-1], nums2[split2_i-1])
                    if (split1_i == len(nums1)):
                        r = nums2[split2_i]
                    elif (split2_i == len(nums2)):
                        r = nums1[split1_i]
                    else:
                        r = min(nums1[split1_i], nums2[split2_i])
                    return (l+r)/2.0