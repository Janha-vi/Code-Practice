class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        integer = 0
        i = 0
        while i < len(s):
            if i < len(s)-1 and letter[s[i]] < letter[s[i+1]]:
                integer += letter[s[i+1]] - letter[s[i]]
                i+=2
            else:
                integer += letter[s[i]]
                i+=1
        return integer            




                           
