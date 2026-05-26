class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # ans=[]

        # for i in range(len(nums)):
        #     if i+k<=len(nums):
        #         crnt_window=nums[i:i+k]
        #         max_val=max(crnt_window)
        #         ans.append(max_val)
        # return ans

        dq=deque()
        ans=[]

        for i in range(len(nums)):
            if dq and dq[0]<=i-k:
                dq.popleft()
            
            while dq and nums[dq[-1]]<nums[i]:
                dq.pop()
            
            dq.append(i)
            
            if i>=k-1:
                ans.append(nums[dq[0]])
        
        return ans