class Solution:
    def jump(self, nums: List[int]) -> int:
        
        j=0
        farthest=0
        cur_window_len=0

        for i in range(len(nums)-1):
            farthest=max(farthest,i+nums[i])

            if i==cur_window_len:
                j+=1
                cur_window_len=farthest
        
        return j