class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # l = 0 
        # for r in range(len(nums)):
        #     if nums[r] == nums[l]:
        #         if r - l > 1:
        #             while nums[l] == nums[r]:
        #                 r+=1
        #             nums[r - 1] = nums[r]
        #             l = r            
        # return l + 1
        j = 1
        for i in range(1, len(nums)):
            if j == 1 or nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
        return j       