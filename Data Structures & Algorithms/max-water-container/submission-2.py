class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # max_ans=0

        # for i in range(len(heights)):
        #     for j in range(i+1,len(heights)):
        #         h=min(heights[i],heights[j])
        #         w=abs(i-j)
        #         max_ans=max(max_ans,h*w)
        
        # return max_ans

        l=0
        r=len(heights)-1
        max_ans=0
        while l<=r:
            max_ans=max(max_ans,min(heights[l],heights[r])*abs(l-r))
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        
        return max_ans