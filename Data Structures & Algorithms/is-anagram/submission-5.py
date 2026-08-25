
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        cn_s=defaultdict()
        cn_t=defaultdict()

        for i in range(len(s)):
            if s[i] not in cn_s:
                cn_s[s[i]]=1
            else:
                cn_s[s[i]]+=1
        
        for j in range(len(t)):
            if t[j] not in cn_t:
                cn_t[t[j]]=1
            else:
                cn_t[t[j]]+=1
        
        if cn_s==cn_t:
            return True
        else:
            return False