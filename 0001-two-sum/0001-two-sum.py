class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nmap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in nmap:
                return [nmap[complement],i]
            nmap[nums[i]]=i
        return []        
                
                