class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_ind={}

        for i,c in enumerate(s):
            last_ind[c]=i
        
        res=[]
        end=0
        size=0
        for i,c in enumerate(s):
            size+=1
            if last_ind[c]>end:
                end=last_ind[c]
            
            if i==end:
                res.append(size)
                size=0
        
        return res