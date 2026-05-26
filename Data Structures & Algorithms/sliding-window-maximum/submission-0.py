class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]

        for i in range(len(nums)):
            if i+k<=len(nums):
                crnt_window=nums[i:i+k]
                max_val=max(crnt_window)
                ans.append(max_val)
        return ans