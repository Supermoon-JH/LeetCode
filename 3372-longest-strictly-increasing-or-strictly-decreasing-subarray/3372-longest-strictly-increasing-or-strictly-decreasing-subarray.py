class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # max_num = 0

        # for i in range(len(nums)):
        #     cur_num = 1
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] > nums[j - 1]:   
        #             cur_num += 1   
        #         else:
        #             break
        #     max_num = max(max_num, cur_num)

        # for i in range(len(nums)):
        #     cur_num = 1
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] < nums[j - 1]:   
        #             cur_num += 1   
        #         else:
        #             break
        #     max_num = max(max_num, cur_num)

        # return max_num
        increasing_length, decreasing_length, max_length = 1, 1, 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increasing_length += 1
                decreasing_length = 1
                max_length = max(increasing_length, max_length)
            elif nums[i] < nums[i - 1]:
                decreasing_length += 1
                increasing_length = 1
                max_length = max(max_length, decreasing_length)
            else:
                increasing_length, decreasing_length = 1, 1
                
        return max_length