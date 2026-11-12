class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        tar=sum(nums)//k
        if sum(nums)%k!=0:
            return False
            
        visit=[False]*(len(nums))

        if nums[0]>tar:
            return False

        def helper(i, cur_sum, k_remaining):
            if k_remaining == 1:
                return True
                
            if cur_sum == tar:
                # Successfully formed one subset, move on to the next one
                return helper(0, 0, k_remaining - 1)

            for j in range(i, len(nums)):
                if not visit[j] and cur_sum + nums[j] <= tar:
                    visit[j] = True
                    if helper(j + 1, cur_sum + nums[j], k_remaining):
                        return True
                    visit[j] = False

            return False

        return helper(0, 0, k)