class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tracker={}

        l=0
        ans=0
        for r in range(len(s)):
            if s[r] not in tracker:
                tracker[s[r]]=1
            else:
                tracker[s[r]]+=1

            max_freq=max(tracker.values())
            
            while (r-l+1)-max_freq>k:
                tracker[s[l]]-=1
                l+=1
            
            ans=max(ans,r-l+1)
        
        return ans