class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        s_set=set()
        l=0
        ans=0
        for r in range(len(s)):

            if s[r] in s_set:
                while True:
                    if s[r] not in s_set:
                        break
                    else:
                        s_set.remove(s[l])
                        l+=1
            
            s_set.add(s[r])
            ans=max(ans,r-l+1)
        
        return ans
