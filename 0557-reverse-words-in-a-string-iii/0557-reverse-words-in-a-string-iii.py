class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = s.split()
        r = ""
        for i in range(len(lst)):
            if i == len(lst)-1:
                r = r + lst[i][::-1]
            else:
                r = r + lst[i][::-1] + " "
        
        return r