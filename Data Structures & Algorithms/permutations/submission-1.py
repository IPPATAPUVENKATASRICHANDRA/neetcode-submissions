class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        glb=[]

        def bt_per(i,ans):

            if len(ans)==len(nums):
                glb.append(ans[:])
                return
        
            for j in range(0,len(nums)):
                if nums[j] not in ans:
                    ans.append(nums[j])
                    bt_per(i+1,ans)
                    ans.pop()
            

        bt_per(0,[])
        return glb