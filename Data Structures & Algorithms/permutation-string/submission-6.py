class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k=len(s1)

        for i in range(len(s2)-k+1):
            s_w=s2[i:i+k]
            if sorted(s_w)==sorted(s1):
                return True
        
        return False