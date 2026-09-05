class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        glb=[]

        def bt_cs(ans,st,total):
            if total==target:
                glb.append(ans[:])

            if total>target:
                return
            
            for i in range(st,len(nums)):
                ans.append(nums[i])
                bt_cs(ans,i,total+nums[i])
                ans.pop()
        
        bt_cs([],0,0)

        return glb

