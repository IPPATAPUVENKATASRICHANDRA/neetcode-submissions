class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        mem={}
        def helper(i, j, k):

            if k == len(s3):
                return True
            
            if (i,j,k) in mem:
                return mem[(i,j,k)]

            res=False

            if i < len(s1) and s1[i] == s3[k]:
                res=helper(i + 1, j, k + 1)
                    

            if j < len(s2) and s2[j] == s3[k]:
                res=helper(i, j + 1, k + 1)
                
            mem[(i,j,k)]=res

            return mem[(i,j,k)]

        return helper(0, 0, 0)