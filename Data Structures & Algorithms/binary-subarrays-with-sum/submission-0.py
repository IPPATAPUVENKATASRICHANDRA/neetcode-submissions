class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        pref_sum=0
        count={0:1}
        ans=0

        for i in nums:
            pref_sum+=i
            ans+=count.get(pref_sum-goal,0)
            count[pref_sum]=count.get(pref_sum,0)+1
        
        return ans

