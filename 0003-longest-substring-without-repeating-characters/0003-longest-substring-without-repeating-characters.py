class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        tempMap = {} #str : len
        for i in range(len(s)):
            tempStr = s[i]
            tempMap[tempStr] = len(tempStr)
            for j in range(i + 1, len(s)):
                temp = tempStr
                tempStr = tempStr + s[j]
                #print(temp, tempStr)
                if s[j] not in temp:
                    tempMap[tempStr] = len(tempStr)
                else:
                    break
        #print(tempMap)
        return max(tempMap.values())
                
            
        