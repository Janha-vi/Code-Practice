class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        r = 0 
        for i in range(m, len(nums1)):
            if nums1[i] == 0:
                nums1[i] = nums2[r]
                r+=1
        return nums1.sort()        