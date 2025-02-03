class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_num = 0

        for i in range(len(nums)):
            cur_num = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[j - 1]:   
                    cur_num += 1   
                else:
                    break
            max_num = max(max_num, cur_num)

        for i in range(len(nums)):
            cur_num = 1
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[j - 1]:   
                    cur_num += 1   
                else:
                    break
            max_num = max(max_num, cur_num)

        return max_num