from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        valid=[0]*len(strs)
        ans=[]

        for i in range(0,len(strs)):
            if valid[i]==1:
                continue

            cnt_one=Counter(strs[i])
            ans_apnd=[strs[i]]
            valid[i]=1

            for j in range(i+1,len(strs)):
                cnt_two=Counter(strs[j])
                if valid[j]!=1 and cnt_one==cnt_two:
                    ans_apnd.append(strs[j])
                    valid[j]=1
            ans.append(ans_apnd)
            ans_apnd=[]
        
        return ans



