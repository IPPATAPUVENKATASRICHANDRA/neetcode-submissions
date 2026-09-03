class TimeMap:

    def __init__(self):
        self.store=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        
        vals=self.store[key]
        ans=''
        for v,t in vals:
            if t<=timestamp:
                ans= v
            else:
                break
        
        return ans
        
