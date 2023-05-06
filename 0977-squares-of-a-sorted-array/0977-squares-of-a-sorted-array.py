class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rtn = []
        for i in nums:
            rtn.append(i*i)
        rtn.sort()
        return rtn
            