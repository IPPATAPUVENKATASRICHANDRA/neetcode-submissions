class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # pos=[]
        # neg=[]

        # ans=[0]*len(nums)
        # l=0
        # r=0
        # for i in nums:
        #     if i>0:
        #         pos.append(i)
        #     else:
        #         neg.append(i)
        

        # for i in range(len(nums)):
        #     if i%2==0:
        #         ans[i]=pos[l]
        #         l+=1
        #     else:
        #         ans[i]=neg[r]
        #         r+=1
        # return ans
        

        l=0
        r=1
        ans=[0]*len(nums)

        for k in range(len(nums)):
            if nums[k]>0:
                ans[l]=nums[k]
                l+=2
            else:
                ans[r]=nums[k]
                r+=2
        return ans