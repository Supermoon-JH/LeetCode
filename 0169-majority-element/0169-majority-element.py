class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n = len(nums)
        # freq = defaultdict(int)

        # for i in nums:
        #     freq[i] += 1

        # for key, value in freq.items():
        #     if value > math.floor(n / 2):
        #         return key

        nums.sort()
        return nums[math.floor(len(nums) / 2)]