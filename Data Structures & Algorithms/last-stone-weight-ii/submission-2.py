class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        # if len(stones)<=0:
        #     return 0
        
        # if len(stones)==1:
        #     return stones[0]
        # if len(stones)==2:
        #     stones.sort()
        #     return stones[0]-stones[1]

        # stones.sort(reverse=True) 
        # n=len(stones)
        # while len(stones)>1:
        #     print(stones)
        #     s1=stones.pop(0)
        #     s2=stones.pop(0)
        #     new_s=abs(s1-s2)
        #     if new_s>0:
        #         stones.append(new_s)
        #         stones.sort(reverse=True)
        
        # return stones[0] if len(stones) == 1 else 0

        sum_stones= sum(stones)
        tar=math.ceil(sum_stones/2)

        dp={}
        def dfs(i,total):   
            if total>=tar or i==len(stones):
                return abs(total-(sum_stones-total))
            
            if (i,total) in dp:
                return dp[(i,total)]
            
            dp[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))
            return dp[(i, total)]

        return dfs(0, 0)



