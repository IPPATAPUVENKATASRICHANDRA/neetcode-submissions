class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[-1] = nums[-1]
        cur_suf_sum = nums[-1]

        for i in range(n - 2, -1, -1):
            cur_suf_sum += nums[i]
            dp[i] = max(cur_suf_sum, dp[i + 1])

        best = nums[0]
        cur_prf_sum = 0
        pref_sum = 0

        for i in range(n):
            cur_prf_sum = max(cur_prf_sum, 0) + nums[i]
            best = max(best, cur_prf_sum)

            pref_sum += nums[i]
            if i + 1 < n:
                best = max(best, pref_sum + dp[i + 1])

        return best