class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        tempMap = {}
        for i, j in enumerate(numbers):
            d = target - j
            if d in tempMap:
                return [tempMap[d] + 1, i + 1]
            tempMap[j] = i
        return
