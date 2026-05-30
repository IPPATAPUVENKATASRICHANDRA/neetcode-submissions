class TimeMap:

    def __init__(self):
        self.d={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.d:
            self.d[key]=[]
        
        self.d[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res=''
        d_values=self.d.get(key,[])

        l,r=0,len(d_values)-1

        while l<=r:
            mid=(l+r)//2

            if d_values[mid][1]<=timestamp:
                res=d_values[mid][0]
                l=mid+1
            else:
                r=mid-1
        
        return res
