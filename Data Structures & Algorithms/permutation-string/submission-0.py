from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_count=Counter(s1)
        print(s1_count)
        window_size=len(s1)
        s2_count={}
        l=0
        for r in range(len(s2)):
            s2_count[s2[r]]=s2_count.get(s2[r],0)+1
            print(s2_count)
                
            while (r-l+1)>window_size:
                s2_count[s2[l]]-=1
                if s2_count[s2[l]]==0:
                    s2_count.pop(s2[l])
                l=l+1
            
            if s1_count==s2_count:
                return True


        return False

            