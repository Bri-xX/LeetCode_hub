class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        remainder = k % len(nums)
        #sub1 = nums[:len(nums) - remainder]
        #sub2 = nums[len(nums) - remainder:]
        #nums = sub2 + sub1
        #reverse the list first
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
            
        #reverse the first k
        l, r = 0, remainder - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        
        #reverse the rest
        l, r = remainder, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1