class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        
        mem={}
        def helper(i,j):
            if i==len(word1):
                return len(word2)-j
            if j==len(word2):
                return len(word1)-i
            
            if (i,j) in mem:
                return mem[(i,j)]
        
            if word1[i]==word2[j]:
                return helper(i+1,j+1)

            # Delete
            delete = helper(i+1, j)

            # Insert
            insert = helper(i, j+1)

            # Replace
            replace = helper(i+1, j+1)

            mem[(i,j)]= 1 + min(delete, insert, replace)

            return mem[(i,j)]
        
        return helper(0,0)