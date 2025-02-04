class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        
        # num_list = [nums[0]]
        # len_list = []

        # for i in range(1, len(nums)):
        #     if nums[i - 1] < nums[i]:
        #         num_list.append(nums[i])
        #         if i == len(nums) - 1:
        #             len_list.append(sum(num_list))
        #     else:
        #         len_list.append(sum(num_list))
        #         num_list = [nums[i]]

        # return max(len_list)

        max_sum = 0
        cur_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                max_sum = max(max_sum, cur_sum)
                cur_sum = 0
            cur_sum += nums[i]
        
        return max(max_sum, cur_sum)