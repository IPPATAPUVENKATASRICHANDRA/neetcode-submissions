class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        totalsum = sum(nums)
        mem = {}

        def dfs(i, arr):
            key = (i, sum(arr))

            if key in mem:
                return mem[key]

            if totalsum - sum(arr) == sum(arr):
                mem[key] = True
                return True

            if i == len(nums):
                mem[key] = False
                return False

            if dfs(i + 1, arr):
                mem[key] = True
                return True

            if dfs(i + 1, arr + [nums[i]]):
                mem[key] = True
                return True

            mem[key] = False
            return False

        return dfs(0, [])