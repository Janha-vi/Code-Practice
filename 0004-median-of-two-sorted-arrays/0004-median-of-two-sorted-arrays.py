import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
    
    # Find the length of the combined array
        l = len(nums)
    
    # If the length is odd, return the middle element
        if l % 2 != 0:
            x = int(l // 2)
            return nums[x]
    
    # If the length is even, return the average of the two middle elements
        else:
        # Two middle elements
            mid1 = (l // 2) - 1
            mid2 = l // 2
            return (nums[mid1] + nums[mid2]) / 2.0


        