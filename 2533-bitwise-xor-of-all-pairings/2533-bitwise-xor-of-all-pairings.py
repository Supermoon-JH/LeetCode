class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        freq = {}
        for i in nums1:
            freq[i] = freq.get(i, 0) + len(nums2)

        for i in nums2:
            freq[i] = freq.get(i, 0) + len(nums1)

        answer = 0
        for i in freq:
            if freq[i] % 2:
                answer ^= i 

        return answer

        # answer = 0
        # for i in range(len(nums3)):
        #     if i == 0:
        #         answer = nums3[i]
        #     else:
        #         answer ^= nums3[i]
        # return answer

        # dp = [0] * len(nums3)
        # for i in range(len(nums3)):
        #     if i == 0:
        #         dp[i] = nums3[i]
        #     else:
        #         dp[i] = dp[i - 1] ^ nums3[i]

        # return dp[-1]
        # Memory Limit Exceeded