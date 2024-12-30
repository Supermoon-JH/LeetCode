class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + [0] * (high)
        
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]

        answer = sum(dp[low: high + 1])
        if answer >= 10 ** 9 + 7:
            return answer % (10 ** 9 + 7)

        return sum(dp[low: high + 1])
