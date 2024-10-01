class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dit = {}
        n = len(nums)
        for i in nums:
            if i not in dit:
                dit[i] = 1
            else:
                dit[i] += 1

        for k, v in dit.items():
            if dit[k] > (n/2):
                return k