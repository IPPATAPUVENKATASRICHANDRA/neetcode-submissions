class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        
        else:
            s_cnt={}
            t_cnt={}

            for i in range(len(s)):
                if s[i] not in s_cnt:
                    s_cnt[s[i]]=1
                else:
                    s_cnt[s[i]]+=1

            for i in range(len(t)):
                if t[i] not in t_cnt:
                    t_cnt[t[i]]=1
                else:
                    t_cnt[t[i]]+=1

            if s_cnt==t_cnt:
                return True
            else:
                return False