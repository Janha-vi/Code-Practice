class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        mini = min(len(first),len(last))
        i = 0
        while i<mini and first[i] == last[i]:
            i+=1

        if i == 0:
            print(" ")
        return first[:i]            