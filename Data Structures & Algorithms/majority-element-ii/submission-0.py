from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n=len(nums)

        cnt=Counter(nums)
        ans=[]
        print(cnt)
        for key,val in cnt.items():
            if val>n//3:
                ans.append(key)
        
        return ans