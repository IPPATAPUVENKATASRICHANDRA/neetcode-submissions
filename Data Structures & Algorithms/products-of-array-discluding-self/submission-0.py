import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            pref_prod=math.prod(nums[:i])
            suf_prod=math.prod(nums[i+1:])
            ans.append((pref_prod*suf_prod))
        return ans

