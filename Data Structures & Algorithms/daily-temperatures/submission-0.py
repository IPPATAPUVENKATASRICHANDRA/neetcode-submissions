class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n

        for i in range(n):
            cnt=0
            for j in range(i+1,n):
                cnt+=1
                if temperatures[i]<temperatures[j]:
                    ans[i]=cnt
                    break
        return ans

