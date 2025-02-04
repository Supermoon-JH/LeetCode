class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        num_list = [nums[0]]
        len_list = []

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                num_list.append(nums[i])
                if i == len(nums) - 1:
                    len_list.append(sum(num_list))
            else:
                len_list.append(sum(num_list))
                num_list = [nums[i]]

        return max(len_list)