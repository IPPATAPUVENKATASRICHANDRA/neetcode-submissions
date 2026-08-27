from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_val=Counter(nums)
        val_tup=list(cnt_val.items())
        val_tup.sort(key=lambda x: x[1], reverse=True)
      
        res=[]
        cnt=0

        for ke,val in val_tup:
            cnt+=1
            res.append(ke)

            if cnt==k:
                return res

        return res
