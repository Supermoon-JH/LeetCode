class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # if len(nums) < 4:
        #     return 0
        
        # answer = 0
        # comb = list(permutations(nums, 4))
        
        # for i in comb:
        #     if i[0] * i[1] == i[2] * i[3]:
        #         answer += 1
        
        # return answer
        # memory limit exceeded

        # if len(nums) < 4:
        #     return 0
        
        # answer = 0
        # comb = list(combinations(nums, 4))
    
        # for i in comb:
        #     freq = defaultdict(int)
        #     two_num = list(combinations(i, 2))
        #     for j in two_num:
        #         product = j[0] * j[1]
        #         freq[product] += 1
        #     for key, value in freq.items():
        #         if value == 2:
        #             answer += 8

        # return answer
        # time limit exceeded
        
        if len(nums) < 4:
            return 0
        
        answer = 0
        freq = defaultdict(int)
        nums_len = len(nums)

        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                product = nums[i] * nums[j]
                freq[product] += 1
        
        for i in freq.values():
            pairs = i * (i - 1) // 2
            answer += pairs * 8

        return answer