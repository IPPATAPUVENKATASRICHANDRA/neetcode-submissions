class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]
        
        if len(nums)==2:
            return max(nums)

    
        def dfs(i, arr):
            if i >= len(arr):
                return 0

            if i in mem:
                return mem[i]

            mem[i] = max(
                dfs(i + 1, arr),               
                arr[i] + dfs(i + 2, arr)      
            )

            return mem[i]

        # Case 1: don't rob last house
        arr1 = nums[:-1]
        mem = {}
        val1 = dfs(0, arr1)

        # Case 2: don't rob first house
        arr2 = nums[1:]
        mem = {}
        val2 = dfs(0, arr2)

        return max(val1, val2)


