class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_val=float('-inf')

        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                leng=min(heights[i],heights[j])
                bret=abs((i)-(j))
                max_val=max(max_val,leng*bret)
        
        return max_val
