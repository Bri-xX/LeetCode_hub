class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #idea: move every non-zero element to the left
        i = 0
        for j in range(len(nums)):
            if nums[j]:
                nums[i], nums[j] = nums[j],  nums[i]
                i += 1
        