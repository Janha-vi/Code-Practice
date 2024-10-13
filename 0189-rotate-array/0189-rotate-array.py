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

        tempe = 0  
        a = 0 
        b = k-1 
        while a < b:
            tempe = nums[b]
            nums[b] = nums[a]
            nums[a] = tempe
            b-=1
            a+=1

        tempee = 0
        c = k
        d = len(nums)-1
        while c < d:
            tempee = nums[d]
            nums[d] = nums[c]
            nums[c] = tempee
            d-=1
            c+=1    
        return nums    