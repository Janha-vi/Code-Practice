class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l = 0
        r = len(nums)-1

        while l < r:
            nums[l] , nums[r] = nums[r], nums[l]
            r-=1
            l+=1
  
        l = 0 
        r = k-1 
        while l < r:
            nums[l] , nums[r] = nums[r], nums[l]
            r-=1
            l+=1

        l = k
        r = len(nums)-1
        while l < r:
            nums[l] , nums[r] = nums[r], nums[l]
            r-=1
            l+=1    
        return nums    