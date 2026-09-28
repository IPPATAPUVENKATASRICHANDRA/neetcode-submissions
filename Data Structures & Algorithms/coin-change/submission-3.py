class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        # ans=float('inf')


        # def backtrack(remaining, count):
        #     nonlocal ans

        #     if remaining == 0:
        #         ans = min(ans, count)
        #         return

        #     if remaining < 0:
        #         return

        #     for coin in coins:
        #         backtrack(remaining - coin, count + 1)

        # backtrack(amount, 0)

        # return -1 if ans == float('inf') else ans

        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]

            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))

            memo[amount] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins