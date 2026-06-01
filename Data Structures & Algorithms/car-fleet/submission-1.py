class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars=sorted(zip(position,speed),reverse=True)


        flt=0
        maxtime=0
        for pos,spd in cars:
            time=(target-pos)/spd

            if time>maxtime:
                flt+=1
                maxtime=time
        
        return flt