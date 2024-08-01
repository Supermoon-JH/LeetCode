class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        value = None
        
        for i in range(len(nums)):
            if nums[i] != value:
                nums[k] = nums[i]
                k += 1
                value = nums[i]
        
        for i in range(k, len(nums)):
            nums[i] = '_'
        
        return k