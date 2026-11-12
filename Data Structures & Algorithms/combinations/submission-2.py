class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # we have a global arr to store
        # n=3 is the loop 
        # k tells each subset length 
        #   -
    #     1   2   3 
    #    2 3 1 3 1 2 
      
    #   [1,2][1,3][2,3]

      # like that branch goes , excluding the duplicates and no repeation    
        glb=[]
        def helper(ind,cur):

            if len(cur)==k:
                glb.append(list(cur))
                return 
            for i in range(ind,n+1):
                if i in cur:
                    continue
                cur.append(i)
                helper(i+1,cur)
                cur.pop()
        
        helper(1,[])

        return glb
        