class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] will store the minimum number of square numbers that sum to i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: 0 requires 0 squares
        
        for i in range(1, n + 1):
            # Try all possible square numbers less than or equal to i
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
                
        return dp[n]