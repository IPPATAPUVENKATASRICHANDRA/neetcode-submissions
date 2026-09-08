class Solution:
    def partition(self, s: str) -> List[List[str]]:

        glb=[]

        def bt_par(i,p_s):
            
            if i==len(s):
                glb.append(p_s[:])

            for j in range(i,len(s)):
                p=s[i:j+1]
                if p==p[::-1]:
                    p_s.append(p)
                    bt_par(j+1,p_s)
                    p_s.pop()

        
        bt_par(0,[])

        return glb
            
