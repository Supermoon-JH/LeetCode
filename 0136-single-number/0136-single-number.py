class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # new = [0] * (max(nums) + 1)
        
        # for i in nums:
        #     new[i] += 1

        # for i in range(len(new)):
        #     if new[i] == 1:
        #         return i

        new = dict()
        
        for i in nums:
            new[i] = new.get(i, 0) + 1

        for i, j in new.items():
            if j == 1:
                return i
            