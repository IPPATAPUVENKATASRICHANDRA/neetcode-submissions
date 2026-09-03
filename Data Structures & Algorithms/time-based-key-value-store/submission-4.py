class TimeMap:

    def __init__(self):
        self.store=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        
        # vals=self.store[key]
        # ans=''
        # for v,t in vals:
        #     if t<=timestamp:
        #         ans= v
        #     else:
        #         break
        
        # return ans
        vals=self.store[key]
        l=0
        r=len(vals)-1
        ans=''
        while l<=r:
            mid=(l+r)//2
            if vals[mid][1]<=timestamp:
                ans=vals[mid][0]
                l=mid+1
            else:
                r=mid-1
        
        return ans

        
