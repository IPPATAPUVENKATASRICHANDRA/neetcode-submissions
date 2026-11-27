class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        ind=set()
        for t in triplets:
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                continue
            
            for i,v in enumerate(t):
                if v==target[i]:
                    ind.add(i)
            

        return True if len(ind)==3 else False
        
            