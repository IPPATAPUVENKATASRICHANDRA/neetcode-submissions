class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l=0
        ans_sum=0
        min_len=float('inf')
        for r in range(len(nums)):
            ans_sum+=nums[r]

            while l<=r and ans_sum>=target:
                min_len=min(min_len,r-l+1)
                ans_sum-=nums[l]
                l+=1

        return min_len if min_len!=float('inf') else 0


