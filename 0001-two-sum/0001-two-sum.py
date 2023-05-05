class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tempMap = {}
        for i, j in enumerate(nums):
            d = target - j
            if d in tempMap:
                return [tempMap[d], i]
            tempMap[j] = i
        return 
            


