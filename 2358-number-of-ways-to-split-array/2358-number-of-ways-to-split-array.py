class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # answer = 0
        # n = len(nums)

        # for i in range(n - 1):
        #     if sum(nums[:i + 1]) >= sum(nums[i + 1:]):
        #         answer += 1

        # return answer
        # Time Limit Exceeded

        answer = 0
        n = len(nums)
        sum_nums = sum(nums)
        prefix = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix[i] += prefix[i - 1] + nums[i - 1]  

        for i in range(n - 1):
            if prefix[i + 1] >= sum_nums - prefix[i + 1]:
                answer += 1

        return answer