class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        mem={}
        def dfs(i):
            if i < 0:
                return False

            if i >= len(nums):
                return False

            if i == len(nums) - 1:
                return True

            if nums[i] == 0:
                return False
            
            if i in mem:
                return mem[i]

            for jump in range(1, nums[i] + 1):
                if dfs(i+jump):
                    mem[i]=True
                    return True
                    
            mem[i]=False
            return False

        if dfs(0):
            return True

        else:
            return False