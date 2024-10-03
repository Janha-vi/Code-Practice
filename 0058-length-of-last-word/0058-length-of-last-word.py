class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        r = 0
        last = len(s)-1
        # while last > 0:
        #     if s[last] == " ":
        #         last -= 1
        #     else:
        #         last = len(s)    
        #     break
        
        # Replace the above 6 (!!!!) lines with this one line:
        while s[last] == " ": last-=1

        # Gregg solution
        # for i in range(last+1):
        #     if s[i] != " ":
        #         count+=1
        #     else:
        #         count = 0
        # return count         

        while r < last:
            if s[r] == " ":
                count = 0
            else: 
                count+=1 
            r+=1    
                
        return count+1         
        