import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prd=math.prod(nums)
        # ans=[]
        # for i in range(len(nums)):
        #     pref=math.prod(nums[:i])
        #     suf=math.prod(nums[i+1:])
        #     ans.append(pref*suf)

        # return ans
        n = len(nums)
        ans = [1] * n

        pref = 1
        for i in range(n):
            ans[i] = pref
            pref *= nums[i]

        suf = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suf
            suf *= nums[i]

        return ans