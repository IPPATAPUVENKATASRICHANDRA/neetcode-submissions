class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        if sum(nums) % k != 0:
            return False

        nums.sort(reverse=True)

        used = [False] * len(nums)
        tar = sum(nums) // k


        def helper(i, par,cnt):


            if cnt == k:
                return True

            if par == tar:
                return helper(0, 0,cnt+1)
            
            for j in range(i, len(nums)):

                if not used[j] and par + nums[j] <= tar:

                    used[j] = True

                    if helper(j + 1, par + nums[j],cnt):
                        return True

                    used[j] = False

            return False

        return helper(0,0,0)