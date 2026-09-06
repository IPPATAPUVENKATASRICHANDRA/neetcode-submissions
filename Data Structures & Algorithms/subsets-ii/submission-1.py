class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        glb=[]

        def bt_swd(st,ans):
            
            if ans[:] not in glb:
                glb.append(ans[:])

            for i in range(st,len(nums)):
                ans.append(nums[i])
                bt_swd(i+1,ans)
                ans.pop()
        
        bt_swd(0,[])
        return glb